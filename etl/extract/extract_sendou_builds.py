from bs4 import BeautifulSoup
import requests
import time


# defining constants:
SENDOU_BUILDS_URL = "https://sendou.ink/builds"
SENDOU_BASE_URL = "https://sendou.ink"


# function that returns the data extracted from sendou as a data frame


def extract_sendou_data():
    # call function that returns a
    # list of paths to each weapon's page of builds
    # call function returns the dataframe
    return None


# function to find paths for weapon build pages
def weapon_build_paths():
    # making a request to 'https://sendou.ink/builds'
    soup = BeautifulSoup(make_request(SENDOU_BUILDS_URL).text, "html.parser")

    paths = []  # empty list for storing paths
    weapon_names = []  # empty list for storing weapon names

    all_links = soup.find_all("a")  # list of all hyperlinks on the page

    # loop through all the links
    for link in all_links:
        path, weapon_name = search_for_build_path(link)
        paths = add_to_list(paths, path)
        weapon_names = add_to_list(weapon_names, weapon_name)
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


def add_to_list(the_list, element):
    if element is not None:
        the_list.append(element)
    return the_list


# function to create a dataframe from the the weapon build data
def create_weapon_build_df():
    return None


# function that takes in a site, makes a request then returns the response
def make_request(URL):
    try:
        # sending a get request to a URL, wait 10 seconds max for a response
        response = requests.get(URL, timeout=10)
        # if the status code is not ok, return an error
        if response.status_code != 200:
            return {
                "status": "error",
                "error": "Request failed as status code is not 200",
            }
        # if succesful return response
        return response
    except Exception:
        # return an error if something else goes wrong with the request
        return {"status": "error", "error": "An unknown error has occurred"}
