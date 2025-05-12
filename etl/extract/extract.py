import pandas as pd
from etl.extract.extract_sendou_builds import extract_sendou_data
from etl.extract.extract_inkipedia import extract_inkipedia
from etl.extract.extract_inkipedia_images import extract_main_weapon_images
from etl.extract.extract_ink_ability_images import extract_ability_images
from etl.extract.extract_ink_special_images import extract_specials_images
from etl.extract.extract_ink_sub_images import extract_subs_images


# function extract all data from sendou and inkepedia
def extract_data():
    # extract builds as a dataframe
    builds_df = extract_sendou_data()
    # extract weapon details as a dataframe
    weapons_df = extract_inkipedia()
    # create a series of weapon names
    w_names = weapons_df['Name']
    # extract weapon images as a list
    main_weapon_images = extract_main_weapon_images(w_names)
    # extract ability images as a dataframe
    ability_img_df = extract_ability_images(builds_df)
    # extract special weapon images as a dataframe
    special_img_df = extract_specials_images(weapons_df)
    # extract sub weapon images as a dataframe
    sub_img_df = extract_subs_images(weapons_df)
    # convert main weapon url list ot a dataframe
    weapon_img_df = edit_main_weapon_images(w_names, main_weapon_images)
    # print(main_weapon_images)
    return (builds_df, weapons_df, ability_img_df,
            special_img_df, sub_img_df, weapon_img_df)


# function to convert the series of weapons to a dataframe with urls
def edit_main_weapon_images(w_names, image_urls):
    # convert to a list
    w_names = w_names.tolist()
    w_names_df = pd.DataFrame(w_names, columns=['Weapon Name'])
    # print(w_names_df)
    # first order the weapons alphabetically
    w_names_df = w_names_df.sort_values(by='Weapon Name')
    # reset the index again
    w_names_df.reset_index(drop=True, inplace=True)
    # --- Assistance from ChatGPT ---------------------------------------
    # order the specials
    image_urls = sorted(image_urls, key=lambda img: img.split('/')[-1])
    # -------------------------------------------------------------------
    if len(w_names) != len(image_urls):
        print("THIS ERROR WILL OCCUR WITH TEST MODE!")
        raise ValueError(
            "Number of image URLs does not match the number of main weapons"
        )
    # add a new column called Image URL
    # add the urls here
    w_names_df['Image URL'] = image_urls
    # return the complete dataframe
    return w_names_df
