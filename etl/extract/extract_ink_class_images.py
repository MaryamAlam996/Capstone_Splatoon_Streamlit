from bs4 import BeautifulSoup
import pandas as pd
from etl.extract.url_request import make_request
import time

CLASSES_GALLERY_PATH = (
    'https://splatoonwiki.org/wiki/Category:Splatoon_3_weapon_class_icons'
)


# function to extract all weapon classes images
# from inkipedia as a dataframe
def extract_classes_images(df_weapons):
    print("\nCreating a dataframe of main weapon images...")
    # first call a function that returns all possible weapon classes
    # as a dataframe
    weapon_classes_df = find_class_names(df_weapons)
    # find all image urls for class images
    image_urls = find_all_class_images()
    # add these to the original weapon classes dataframe
    weapon_classes_df = create_class_df(weapon_classes_df, image_urls)
    print(
        "\x1b[32mDone! " +
        str(weapon_classes_df.shape[0]) +
        "/11 \x1b[32mimages found\x1b[0m")
    # check the length
    if weapon_classes_df.shape[0] == 11:
        # return the completed classes dataframe
        return weapon_classes_df
    else:
        raise Exception(
            "Error: Weapon classes data frame only has " +
            str(weapon_classes_df.shape[0]) +
            " classes, some are missing"
        )


# function to find all possible weapon classes
def find_class_names(df_weapons):
    # obtain a series of distinct weapon classes
    weapon_classes = df_weapons['Class'].unique()
    # create a dataframe of distinct weapon classes
    weapon_classes_df = pd.DataFrame(weapon_classes, columns=['Weapon Class'])
    # return this dataframe of weapon classes
    return weapon_classes_df


# function to find all weapon class images
def find_all_class_images():
    # make request to the site
    soup = BeautifulSoup(
        make_request(CLASSES_GALLERY_PATH).text, "html.parser"
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
        image_urls = find_class_image(img, image_urls)
    # return the complete list
    return image_urls


# function to check if the image is a weapon class
# if so add to the list or urls
def find_class_image(img, image_urls):
    src = img.get('src')
    # Check if the 'src' attribute exists and contains 'S3_Icon'
    if src and 'S3_Icon' in src:
        image_urls.append('https:' + src)
    return image_urls


# function to use both the list of images
# and dataframe of weapon classes
# to create a complete dataframe of w_class images
def create_class_df(weapon_classes_df, image_urls):
    # first order the w_classs alphabetically
    weapon_classes_df = weapon_classes_df.sort_values(by='Weapon Class')
    # reset the index again
    weapon_classes_df.reset_index(drop=True, inplace=True)
    # --- Assistance from ChatGPT ---------------------------------------
    # order the specials
    image_urls = sorted(image_urls, key=lambda img: img.split('/')[-1])
    # -------------------------------------------------------------------
    # add a new column called Image URL
    # add the urls here
    weapon_classes_df['Image URL'] = image_urls
    # return the complete dataframe
    return weapon_classes_df
