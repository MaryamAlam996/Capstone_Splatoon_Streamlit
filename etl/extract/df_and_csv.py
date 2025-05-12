# import pandas as pd
from pathlib import Path


# function to convert all the extracted dfs to csvs
# do this to avoid extracting when testing next part of code
# (tranform and load)
def extract_to_csv(df_list):
    # builds_df, weapons_df, ability_img_df,
    # special_img_df, sub_img_df, weapon_img_df
    # --
    # create a list of file names (in the correct order)
    file_names = ['builds', 'weapons',
                  'ability_img', 'special_img', 'sub_img',
                  'weapon_img', 'class_img']
    # --- Assistance from ChatGPT -----------------
    # either access or create a folder called data
    folder = Path('Data')
    folder.mkdir(parents=True, exist_ok=True)
    # for each datafrane and respective file name
    # create the path and create a csv
    for index in range(0, len(df_list)):
        the_path = folder / f"{file_names[index]}.csv"
        df_to_csv(df_list[index], the_path)
    # ---------------------------------------------
    return None


# function to convert to a dataframe to a csv
def df_to_csv(the_df, the_path):
    the_df.to_csv(the_path, index=False)  # remove index columns
    return None
