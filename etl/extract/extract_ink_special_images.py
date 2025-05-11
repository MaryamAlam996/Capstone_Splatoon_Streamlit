from bs4 import BeautifulSoup
import pandas as pd
from etl.extract.url_request import make_request
import time

SPECIALS_GALLERY_PATH = (
    'https://splatoonwiki.org/wiki/Category:Splatoon_3_special_weapon_icons'
)


# function to extract all special weapon images
# from inkipedia as a dataframe
def extract_specials_images(df_weapons):
    print("\nCreating a dataframe of special weapon images...")
    # first call a function that returns all possible special weapons
    # as a dataframe
    special_weapons_df = find_special_names(df_weapons)
    # find all image urls for special images
    image_urls = find_all_special_images()
    # add these to the original specials dataframe
    special_weapons_df = create_special_df(special_weapons_df, image_urls)
    print("\x1b[32mDone! " + str(special_weapons_df.shape[0]) + "/19 \x1b[32mimages found\x1b[0m")
    # check the length
    if special_weapons_df.shape[0] == 19:
        # return the completed abilities dataframe
        return special_weapons_df
    else:
        raise Exception(
            "Error: Special weapons data frame only has " +
            str(special_weapons_df.shape[0]) +
            " Specials, some are missing"
        )


# function to find all possible special weapons
def find_special_names(df_weapons):
    # obtain a series of distinct special weapons
    special_weapons = df_weapons['Special'].unique()
    # create a dataframe of distinct special weapons
    special_weapons_df = pd.DataFrame(special_weapons, columns=['Special'])
    # return this dataframe of special weapons
    return special_weapons_df


# function to find all special weapon images
def find_all_special_images():
    # make request to the site
    soup = BeautifulSoup(
        make_request(SPECIALS_GALLERY_PATH).text, "html.parser"
        )
    # obtain all images
    images = soup.find_all('img')
    image_urls = []  # to store urls
    # pause
    time.sleep(1)
    # loop through images on the page
    for img in images:
        # pause
        time.sleep(0.05)
        # call a function to add the image url to the list
        image_urls = find_special_image(img, image_urls)
    # return the complete list
    return image_urls


# function to check if the image is a special
# if so add to the list or urls
def find_special_image(img, image_urls):
    src = img.get('src')
    if src and 'Special' in src and 'Rainmaker' not in src:
        if 'Splashdown' not in src:
            image_urls.append('https:' + src)
        elif 'Triple' in src:
            image_urls.append('https:' + src)
    return image_urls


# function to use both the list of images
# and dataframe of weapon names
# to create a complete dataframe of ability images
def create_special_df(special_weapons_df, image_urls):
    # first order the specials alphabetically
    special_weapons_df = special_weapons_df.sort_values(by='Special')
    # reset the index again
    special_weapons_df.reset_index(drop=True, inplace=True)
    # --- Assistance from ChatGPT ---------------------------------------
    # order the specials
    image_urls = sorted(image_urls, key=lambda img: img.split('/')[-1])
    # -------------------------------------------------------------------
    # add a new column called Image URL
    # add the urls here
    special_weapons_df['Image URL'] = image_urls
    # return the complete dataframe
    return special_weapons_df
