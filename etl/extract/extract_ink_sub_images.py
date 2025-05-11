from bs4 import BeautifulSoup
import pandas as pd
from etl.extract.url_request import make_request
import time

SUBS_GALLERY_PATH = (
    'https://splatoonwiki.org/wiki/Category:Splatoon_3_sub_weapon_icons'
)


# function to extract all subs weapon images
# from inkipedia as a dataframe
def extract_subs_images(df_weapons):
    print("\nCreating a dataframe of sub weapon images...")
    # first call a function that returns all possible sub weapons
    # as a dataframe
    sub_weapons_df = find_sub_names(df_weapons)
    # find all image urls for sub images
    image_urls = find_all_sub_images()
    # add these to the original subs dataframe
    sub_weapons_df = create_sub_df(sub_weapons_df, image_urls)
    print(
        "\x1b[32mDone! " +
        str(sub_weapons_df.shape[0]) +
        "/14 \x1b[32mimages found\x1b[0m")
    # check the length
    if sub_weapons_df.shape[0] == 14:
        # return the completed abilities dataframe
        return sub_weapons_df
    else:
        raise Exception(
            "Error: Special weapons data frame only has " +
            str(sub_weapons_df.shape[0]) +
            " Subs, some are missing"
        )


# function to find all possible sub weapons
def find_sub_names(df_weapons):
    # obtain a series of distinct sub weapons
    sub_weapons = df_weapons['Sub'].unique()
    # create a dataframe of distinct sub weapons
    sub_weapons_df = pd.DataFrame(sub_weapons, columns=['Sub Weapon'])
    # return this dataframe of sub weapons
    return sub_weapons_df


# function to find all sub weapon images
def find_all_sub_images():
    # make request to the site
    soup = BeautifulSoup(
        make_request(SUBS_GALLERY_PATH).text, "html.parser"
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
        image_urls = find_sub_image(img, image_urls)
    # return the complete list
    return image_urls


# function to check if the image is a sub
# if so add to the list or urls
def find_sub_image(img, image_urls):
    src = img.get('src')
    # Check if the 'src' attribute exists and contains 'Sub'
    # we also want the 'Flat' images
    # also exclude any 'Small fry' images
    if src and 'Sub' in src and 'Flat' in src:
        if 'Smallfry' not in src:
            image_urls.append('https:' + src)
    return image_urls


# function to use both the list of images
# and dataframe of weapon names
# to create a complete dataframe of sub images
def create_sub_df(sub_weapons_df, image_urls):
    # first order the subs alphabetically
    sub_weapons_df = sub_weapons_df.sort_values(by='Sub Weapon')
    # reset the index again
    sub_weapons_df.reset_index(drop=True, inplace=True)
    # --- Assistance from ChatGPT ---------------------------------------
    # order the specials
    image_urls = sorted(image_urls, key=lambda img: img.split('/')[-1])
    # -------------------------------------------------------------------
    # add a new column called Image URL
    # add the urls here
    sub_weapons_df['Image URL'] = image_urls
    # return the complete dataframe
    return sub_weapons_df
