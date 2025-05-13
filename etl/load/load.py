# import pandas as pd
from pathlib import Path


def load_data(all_dfs_tuple):
    load_to_csv(all_dfs_tuple)
    return None


def load_to_csv(df_tuple):
    print("Saving Dataframes as CSVs...")
    # weapons_df (is index 0)
    # (weapons_df, AP_builds_df, Ability_builds_df, ALL_mean_df,
    #  WEAPON_mean_df,
    #   CLASS_mean_df, SUB_mean_df, SPECIAL_mean_df,
    #   ALL_modes_df, WEAPON_modes_df)
    # --
    # create a list of file names (in the correct order)
    file_names = [
        'weapons_details.csv',
        'Ability_Point_builds.csv',
        'Ability_list_builds.csv',
        'All_ability_means.csv',
        'Weapon_ability_means.csv',
        'Weapon_Class_ability_means.csv',
        'Sub_Weapon_ability_means.csv',
        'Special_Weapon_ability_means.csv',
        'Game_mode.csv',
        'Game_mode_by_Weapon.csv'
    ]
    folder = Path('Data')
    folder.mkdir(parents=True, exist_ok=True)
    # for each datafrane and respective file name
    # create the path and create a csv
    for index in range(0, len(df_tuple)):
        the_path = folder / file_names[index]
        df_to_csv(df_tuple[index], the_path)
    print("\x1b[32mDone!\x1b[0m")


# function to convert to a dataframe to a csv
def df_to_csv(the_df, the_path):
    the_df.to_csv(the_path, index=False)  # remove index columns
    return None
