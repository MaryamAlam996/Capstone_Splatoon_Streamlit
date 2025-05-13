import pandas as pd
import time


# transform the weapons df
def transform_weapons_df(data_path):
    # the path of the csv
    the_path = data_path + "/weapons.csv"
    # Load the CSV file as a dataframe
    weapons_df = pd.read_csv(the_path)
    # clean it
    time.sleep(0.5)
    weapons_df = clean_weapons_df(weapons_df)
    print("\x1b[0m" + "-" * 80)
    print("\n")
    time.sleep(0.5)
    weapons_df = enrich_weapons_df(weapons_df, data_path)
    print("\x1b[0m" + "-" * 80)
    return weapons_df


# function to clean and standardize weapons dataframe
def clean_weapons_df(weapons_df):
    print("\x1b[34mCleaning and Standardizing " +
          "\x1b[96mweapons dataframe...\x1b[0m")
    print("\x1b[0m" + "-" * 80)
    # Cleaning
    # Drop columns not needed for analysis
    weapons_df_edit = weapons_df.drop(
        ['Extra_space', 'ID', 'Level', 'Price', 'Introduced'], axis=1)
    print("\x1b[35m>>> Dropped unused columns")
    # Remove weapon reskins (weapon that are identical to others gameplay wise)
    weapons_df_edit_2 = weapons_df_edit[
        ~(
            (weapons_df_edit['Name'] == 'Hero Shot Replica') |
            (weapons_df_edit['Name'] == 'Octo Shot Replica') |
            (weapons_df_edit['Name'] == 'Order Shot Replica') |
            (weapons_df_edit['Name'] == 'Order Blaster Replica') |
            (weapons_df_edit['Name'] == 'Order Roller Replica') |
            (weapons_df_edit['Name'] == 'Orderbrush Replica') |
            (weapons_df_edit['Name'] == 'Order Charger Replica') |
            (weapons_df_edit['Name'] == 'Order Slosher Replica') |
            (weapons_df_edit['Name'] == 'Order Splatling Replica') |
            (weapons_df_edit['Name'] == 'Order Dualie Replicas') |
            (weapons_df_edit['Name'] == 'Order Brella Replica') |
            (weapons_df_edit['Name'] == 'Order Stringer Replica') |
            (weapons_df_edit['Name'] == 'Order Splatana Replica')
        )
    ]
    print(">>> Removed weapon reskins")
    # Standardize:
    # Convert special points to an int
    weapons_df_edit_3 = weapons_df_edit_2.copy()
    weapons_df_edit_3['Special_Points'] = (
        weapons_df_edit_3['Special_Points']
        .str.replace('p', '')
        .astype(int)
    )
    print(">>> Converted Special points to integers\x1b[0m")
    print("Original data frame: \x1b[33m" +
          str(weapons_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(weapons_df.shape[1]) + " columns\x1b[0m")
    print("Cleaned data frame: \x1b[33m" +
          str(weapons_df_edit_3.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(weapons_df_edit_3.shape[1]) + " columns\x1b[0m")
    return weapons_df_edit_3


# enrich the dataframe with image urls of weapons
def enrich_weapons_df(weapons_df, data_path):
    print("\x1b[34mEnriching \x1b[96mweapons dataframe...\x1b[0m")
    print("\x1b[0m" + "-" * 80)
    weapons_df_edit = add_weapon_images(weapons_df, data_path)
    print("\x1b[35m>>> Added main weapon images")
    weapons_df_edit = add_sub_images(weapons_df_edit, data_path)
    print(">>> Added sub weapon images")
    weapons_df_edit = add_special_images(weapons_df_edit, data_path)
    print(">>> Added special weapon images")
    weapons_df_edit = add_class_images(weapons_df_edit, data_path)
    print(">>> Added weapon class images\x1b[0m")
    print("Enriched data frame: \x1b[33m" +
          str(weapons_df_edit.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(weapons_df_edit.shape[1]) + " columns\x1b[0m")
    return weapons_df_edit


# function to add main weapon images to the df
def add_weapon_images(weapons_df, data_path):
    # find the df of images
    weapon_img_df = find_df(data_path+"/weapon_img.csv")
    weapon_img_df = weapon_img_df.rename(columns={'Image URL': 'Weapon_Img'})
    # create a copy to edit
    weapons_df_2 = weapons_df.copy()
    # do a left join to add URLS for only the weapons we want to use
    # join by matching weapon names
    weapons_df_2 = pd.merge(
        weapons_df, weapon_img_df, left_on='Name', right_on='Weapon Name',
        how='left')
    weapons_df_2 = weapons_df_2.drop(
        ['Weapon Name'], axis=1)
    return weapons_df_2


# function to add sub weapon images to the df
def add_sub_images(weapons_df, data_path):
    # find the df of images
    sub_img_df = find_df(data_path+"/sub_img.csv")
    sub_img_df = sub_img_df.rename(columns={'Image URL': 'Sub_Img'})
    # create a copy to edit
    weapons_df_2 = weapons_df.copy()
    # join by matching sub weapon names
    weapons_df_2 = pd.merge(
        weapons_df, sub_img_df, left_on='Sub', right_on='Sub Weapon',
        how='left')
    weapons_df_2 = weapons_df_2.drop(
        ['Sub Weapon'], axis=1)
    return weapons_df_2


# function to add special weapon images to the df
def add_special_images(weapons_df, data_path):
    # find the df of images
    special_img_df = find_df(data_path+"/special_img.csv")
    special_img_df = special_img_df.rename(
        columns={'Image URL': 'Special_Img'}
        )
    # create a copy to edit
    weapons_df_2 = weapons_df.copy()
    # join by matching special weapon names
    weapons_df_2 = pd.merge(
        weapons_df, special_img_df, left_on='Special', right_on='Special',
        how='left')
    return weapons_df_2


# function to add weapon class images to the df
def add_class_images(weapons_df, data_path):
    # find the df of images
    class_img_df = find_df(data_path+"/class_img.csv")
    class_img_df = class_img_df.rename(columns={'Image URL': 'Class_Img'})
    # create a copy to edit
    weapons_df_2 = weapons_df.copy()
    # join by matching weapon class names
    weapons_df_2 = pd.merge(
        weapons_df, class_img_df, left_on='Class', right_on='Weapon Class',
        how='left')
    weapons_df_2 = weapons_df_2.drop(
        ['Weapon Class'], axis=1)
    return weapons_df_2


# find the csv and convert to df to use
def find_df(the_path):
    # Load the CSV file as a dataframe
    weapon_img_df = pd.read_csv(the_path)
    return weapon_img_df
