from bs4 import BeautifulSoup
import requests
import time
# import pandas as pd
# from etl.extract.url_request import make_request
from tqdm import tqdm


HEADERS = {'User-Agent': 'Mozilla/5.0'}

ALL_WEAPONS_SITE = (
    "https://splatoonwiki.org/wiki/List_of_main_weapons_in_Splatoon_3"
)

BASE_PATHS = 'https://splatoonwiki.org'  # Base URL for the Splatoon wiki

TEST_MODE = True


# function to extract all main wain weapon images as
# a list of paths to URLs
# this function takes in weapon names from the weapon
# details dataframe created in extract_inkipedia
def extract_main_weapon_images(w_names):
    # create a session object to make requests with
    session = start_session()
    print("\n")
    print("Finding the weapon pages on inkipedia...")
    # calls a function that returns a list of paths to each weapon page
    path_list = find_all_weapon_pages(session, w_names)
    print("\x1b[32mDone!\x1b[0m\n")
    print("Now finding the main weapon images...")
    # print("-----------------------------------------")
    # calls a function that returns the image urls as a
    image_path_list = find_all_weapon_urls(session, path_list, w_names)
    # print("-----------------------------------------")
    # -------------------------
    # for testing
    if TEST_MODE and len(image_path_list) > 4:
        return image_path_list
    # -------------------------
    # check if list of images length matches weapon list length
    if len(image_path_list) == len(w_names):
        # return the list off images found
        return image_path_list
    else:
        # raise an error otherwise
        raise Exception("Weapon list and image url list lengths don't match")


# function to find paths to each weapon page
def find_all_weapon_pages(session, w_names):
    # using the session to make requests to the site
    response = session.get(ALL_WEAPONS_SITE, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    path_list = []  # empty list
    # find all 'td' objects on the page with all weapons listed
    # these are individual cells in the table
    weapons = soup.find_all('td')
    # remove any repeats to improve speed
    weapons = list(dict.fromkeys(weapons))
    # --------------------------------------
    # for testing do this
    if TEST_MODE is True:
        weapons = weapons[:35]
    # --------------------------------------
    # looping through the list of paths (with a progress bar)
    for w in tqdm(weapons, desc="Finding weapon pages", unit="weapon"):
        # check if the path has a link with a href attribute
        if w.find('a') is not None:
            if w.find('a')['href'] is not None:
                # function to obtain the path and match it with
                # the weapon names we have
                # if match add to the list of paths
                path_list = find_weapon_path(w, path_list, w_names)
    # remove duplicates
    path_list = list(dict.fromkeys(path_list))
    # sort alphabetically
    path_list.sort()
    # pause
    time.sleep(2)
    return path_list


# function to find the path for each weapon and add to the list
def find_weapon_path(w, path_list, w_names):
    w_href = w.find('a')['href']
    # Split the URL to get the last part, which is the weapon name
    w_href_edit = w_href.split('/')[-1]
    w_href_edit = fix_names(w_href_edit)
    # check if w_href_edit matches a weapon in the weapon list
    if w_href_edit in w_names.values:
        time.sleep(0.02)
        # make a list of the urls with a weapon name
        path_list.append(BASE_PATHS + w_href)
    return path_list


# fix weapon names to match the format with the ones if the dataframe
def fix_names(name):
    # Replace underscores with spaces to match the original weapon names
    name = name.replace('_', ' ')
    # Making changes to certain names to be in the right format:
    name = name.replace('Z%2BF', 'Z+F')
    name = name.replace('%2785', "'85")
    name = name.replace('%2789', "'89")
    name = name.replace('%2792', "'92")
    name = name.replace('%2791', "'91")
    # return the edited name
    return name


# function to find the weapon image from each weapon page
def find_all_weapon_urls(session, path_list, w_names):
    image_path_list = []  # empty list to store urls
    # count = 0
    # use a progress bar to track how many urls found
    with tqdm(
        total=len(path_list),           # total number of urls to find
        desc="Finding weapon images",   # printed next to bar
        unit="weapon"
    ) as pbar:
        # loop through each path in the list
        for weapon_path in path_list:
            # pause (this part would often cause errors without)
            time.sleep(1)
            # using the same session make requests
            response = session.get(weapon_path, timeout=30)
            soup = BeautifulSoup(response.text, 'html.parser')
            # call function to find the right image from all images
            image_path_list = find_all_images(soup, image_path_list)
            # when at least one image has been found
            if image_path_list:
                # display the name of the image file found
                pbar.set_postfix({'Found image': (
                    image_path_list[-1].split('/')[-1]
                )})
            # update the progress bar
            pbar.update(1)
    # print a message when done to show how many images where found
    # compared to how many we need
    print(
        "\n\x1b[32mDone! " + str(len(image_path_list)) +
        "/" + str(len(w_names))
        + "\x1b[32m weapon images found\x1b[0m"
    )
    # return the complete list
    return image_path_list


# function to find all the images on the page
# then return the correct image of the weapon
def find_all_images(soup,  image_path_list):
    # find image objects from the page
    images = soup.find_all('img')
    # loop through each until we find the right one
    for img in images:
        # call a function to see if the image is correct
        # returns None otherwise
        image_url = find_image(img)
        # if the right one has been found
        if image_url is not None:
            # add to the list
            image_path_list.append(image_url)
            # stop searching
            break
    # return the full list of images
    return image_path_list


# function to find and return the correct image
def find_image(img):
    # find the URL of the image
    src = img.get('src', '')
    # if the URL includes this
    # it is the right one!
    if '256px-S3' in src:
        # add this to make it usable
        image_url = 'https:' + src
        # return the full url
        return image_url
    else:
        # otherwise return None
        return None


# function to create the session object
def start_session():
    # creating new session object using requests
    session = requests.Session()
    # using the headers
    session.headers.update(HEADERS)
    # return it
    return session

# --- Assistance from ChatGPT -----------------
# code for progress bar created using tqdm
# ---------------------------------------------
