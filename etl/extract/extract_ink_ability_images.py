import pandas as pd
from bs4 import BeautifulSoup
from etl.extract.url_request import make_request
import time

ABILITY_GALLERY_PATH = (
    'https://splatoonwiki.org/wiki/Category:Splatoon_3_ability_icons'
    )


# function extract ability chunk images from inkipedia
# returns a dataframe for abilities and urls
def extract_ability_images(df_builds):
    print("\nCreating a dataframe of ability images...")
    # first call a function that returns all possible abilities
    # as a dataframe
    abilities_df = find_ability_names(df_builds)
    # find all image urls for ability images
    image_urls = find_all_ability_images()
    # add these to the original ability dataframe
    abilities_df = create_ability_df(abilities_df, image_urls)
    print("\x1b[32mDone! " + str(abilities_df.shape[0]) + "/26 \x1b[32mimages found\x1b[0m")
    # check the length
    if abilities_df.shape[0] == 26:
        # return the completed abilities dataframe
        return abilities_df
    else:
        raise Exception(
            "Error: Abilities data frame only has " +
            str(abilities_df.shape[0]) +
            " abilities, some are missing"
        )


# function that using the builds dataframe find all possible ability names
def find_ability_names(df_builds):
    # create pandas series for each gear type's
    # possible options for main abilities
    # ability options for head gear:
    main_1 = df_builds['Main_1'].drop_duplicates()
    # ability options for clothing
    main_2 = df_builds['Main_2'].drop_duplicates()
    # ability options for shoes
    main_3 = df_builds['Main_3'].drop_duplicates()

    # combine to form a series of all possible options (no repeats)
    all_abilities = pd.concat([main_1, main_2, main_3]).drop_duplicates()

    # Convert the series to a dataframe
    # reset the index so we have abilities 0 to 25
    # there should be 26 found in total
    abilities_df = pd.DataFrame(
        all_abilities, columns=['Abilities']).reset_index(drop=True)

    # display(abilities_df)
    # return the dataframe of ability names
    return abilities_df


# function that find all the images of possible abilities
def find_all_ability_images():
    # request to website
    soup = BeautifulSoup(
        make_request(ABILITY_GALLERY_PATH).text, "html.parser"
        )
    # find all images on the page
    images = soup.find_all('img')
    # pause
    time.sleep(1)
    image_urls = []  # empty list to store urls
    # loop through each image on the page
    for img in images:
        # pause
        time.sleep(0.05)
        # call the function to check if the image is for an ability
        # and adds it to the list
        image_urls = find_ability_image(img, image_urls)
    return image_urls


# function to check if the image is of an ability
# if so add to the list or urls
def find_ability_image(img, image_urls):
    src = img.get('src')
    # Check if the 'src' attribute exists and contains 'Ability'
    # We also want to exclude the 'locked' used for when
    # an ability slot is empty
    if src and 'Ability' in src and 'Locked' not in src:
        # add the image URL to the list
        image_urls.append('https:' + src)
    return image_urls


# function to use both the list of images
# and dataframe of ability names
# to create a complete dataframe of ability images
def create_ability_df(abilities_df, image_urls):
    # first order the abilities alphabetically
    abilities_df = abilities_df.sort_values(by='Abilities')
    # reset the index again
    abilities_df.reset_index(drop=True, inplace=True)
    # --- Assistance from ChatGPT ---------------------------------------
    image_urls = sorted(image_urls, key=lambda img: img.split('/')[-1])
    # -------------------------------------------------------------------
    # add a new column called Image URL
    # add the urls here
    abilities_df['Image URL'] = image_urls
    # return the complete dataframe
    return abilities_df
