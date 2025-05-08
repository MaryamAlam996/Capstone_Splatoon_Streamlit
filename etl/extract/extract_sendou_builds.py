from bs4 import BeautifulSoup
# import requests
import time
import pandas as pd
from etl.extract.extract import make_request

# defining constants:
SENDOU_BUILDS_URL = "https://sendou.ink/builds"
SENDOU_BASE_URL = "https://sendou.ink"

DF_COLUMNS = [
    'Weapon_name',
    'Main_1', 'Sub_1', 'Sub_2', 'Sub_3',
    'Main_2', 'Sub_4', 'Sub_5', 'Sub_6',
    'Main_3', 'Sub_7', 'Sub_8', 'Sub_9',
    'game_modes'
]


# function that returns the data extracted from sendou as a data frame
def extract_sendou_data():
    # call function that returns a
    # lists of paths to each weapon's page of builds
    # and it's weapon name
    path_list, weapon_list = weapon_build_paths()
    # call function returns the dataframe for all builds
    df_builds = create_weapon_build_df(path_list, weapon_list)
    return df_builds


# function to find paths for weapon build pages
def weapon_build_paths():
    # making a request to 'https://sendou.ink/builds'
    soup = BeautifulSoup(make_request(SENDOU_BUILDS_URL).text, "html.parser")

    paths = []  # empty list for storing paths
    weapon_names = []  # empty list for storing weapon names

    all_links = soup.find_all("a")  # list of all hyperlinks on the page

    # loop through all the links
    for link in all_links:
        # call function that if the link is for a build
        # return the path and name
        path, weapon_name = search_for_build_path(link)
        # add this path to the list
        paths = add_to_list(paths, path)
        # add this weapon name to the list
        weapon_names = add_to_list(weapon_names, weapon_name)
    # check to see if both lists are of same size
    # so that each weapon has a path
    if len(paths) == len(weapon_names):
        return paths, weapon_names
    else:
        raise Exception("Error: number of paths and weapon names don't match")


# function to find the build paths
def search_for_build_path(link):
    href = link.get("href")  # the href of attribute of <a>
    # make sure that the <a> has href
    if href is not None:
        # if href is not none
        # then continue to check if the link is for a weapon build page
        if href.startswith("/builds/"):
            # if it is then add the base path to the end and return this value
            path = SENDOU_BASE_URL + href
            # also find the text of the link (with strip remove whitespaces)
            text = link.get_text(strip=True)
            # if text is not none assign it to weapon_name
            if text is not None:
                weapon_name = text
            else:
                return None, None
            # brief pause between each path retrieval
            # (avoid overwhelming the website)
            time.sleep(0.1)
            # return the path and weapon name associated with the link
            return path, weapon_name
    return None, None


# function to add an element to a list
# only if its not none
def add_to_list(the_list, element):
    if element is not None:
        the_list.append(element)
    return the_list


# function to create a dataframe from the the weapon build data
def create_weapon_build_df(path_list, weapon_list):
    # Create and empty data frame from the columns already defined
    # this will store all the builds listed on the website
    df_all_weapon_builds = pd.DataFrame(columns=DF_COLUMNS)
    count = 0  # counter for what weapon builds page we are currently on
    # repeat for each weapon path
    for path in path_list:
        # pause for each path
        time.sleep(1)
        # if count > 10:
        #     break
        # make request to the path
        path_soup = BeautifulSoup(make_request(path + '?limit=500').text,
                                  "html.parser")
        # calls a function that returns all the builds of a single weapon
        # as a dataframe
        df_weapon_builds = scrape_all_builds(path_soup, weapon_list, count)
        # append to the dataframe of all weapon builds
        df_all_weapon_builds = pd.concat([df_all_weapon_builds,
                                          df_weapon_builds], ignore_index=True)
        count += 1
    return df_all_weapon_builds


# function to scrape all builds for a single weapon:
def scrape_all_builds(path_soup, weapon_list, count):
    # data frame for all builds for a weapon
    df_weapon_builds = pd.DataFrame(columns=DF_COLUMNS)
    # message to show what weapon we are currently obtaining info from
    print("Scraping builds for: " + weapon_list[count])
    # finds all the builds on the page
    build_entries = path_soup.find_all('div',  class_='build')
    # loops through these
    for build in build_entries:
        # scrape each build
        ability_list, mode_list = scrape_a_build(build)
        # use the lists created to add a new row to the dataframe
        df_weapon_builds.loc[len(df_weapon_builds)] = [weapon_list[count]]
        + ability_list + [mode_list]
    # return all builds for that weapon
    return df_weapon_builds


# function to look at a single build and returns its info
def scrape_a_build(build):
    # create a list of the abilities of a build
    ability_list = extract_abilities(build)
    # create a list of the modes of a build
    mode_list = extract_modes(build)
    # return both
    return ability_list, mode_list


# function to extract game mode info from a build
def extract_modes(build):
    mode_list = []  # create empty list to store modes
    # find all the modes
    modes = build.find('div', class_='build__modes')
    #  check if there are any modes listed
    if modes is None:
        # if none, add this message instead
        # placeholder for now
        mode_list = ['NO MODES LISTED']
    elif modes is not None:
        # if there is modes listed
        # find the image tags for modes
        # as each mode is represented by an image
        img_tags = modes.find_all('img')
        # loop through the found image tags
        for i in img_tags:
            # the alt text is the name of the mode
            alt_text = i['alt']
            # add to the list of modes
            mode_list.append(alt_text)
    # return this list
    return mode_list


# function to extract ability info from a build
def extract_abilities(build):
    # find all abilities
    abilities = build.find_all('div', class_="build__ability readonly")
    ability_list = []  # create empty list to store abilities
    # loop through the found abilities
    for a in abilities:
        # find the image of the ability
        img_tag = a.find('img')
        # find the alt text which has the name
        alt_text = img_tag['alt']
        # add to the list of abilities
        ability_list.append((alt_text))
    # return this list
    return ability_list
