import pandas as pd
import ast
import time


# function to transform the builds df
def transform_builds_df(weapons_df, data_path):
    # the path of the csv
    the_path = data_path + "/builds.csv"
    # Load the CSV file as a dataframe
    builds_df = pd.read_csv(the_path)
    # clean it
    time.sleep(0.5)
    builds_df = clean_builds_df(builds_df)
    # enrich
    print("\n")
    time.sleep(0.5)
    builds_df = enrich_builds_df(builds_df, weapons_df)
    # aggregate
    print("\n")
    time.sleep(0.5)
    build_df_tuple = aggregate_builds_df(builds_df)
    # return the new dfs
    return build_df_tuple


# function to clean builds dataframe
def clean_builds_df(builds_df):
    print("\x1b[34mCleaning \x1b[36mbuilds dataframe...")
    # remove all builds with 'Ability doubler'
    # this ability only appears during splatfest and
    # so cannot be used in regular battles
    builds_df_edit = builds_df[builds_df['Main_2'] != 'Ability Doubler']
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Removed ability doubler")
    # removing builds that have mains of all of the same ability
    # (as these tend to not make very good builds)
    builds_df_edit_2 = builds_df_edit[
        ~(
            (builds_df_edit['Main_1'] == builds_df_edit['Main_2']) &
            (builds_df_edit['Main_2'] == builds_df_edit['Main_3'])
        )
    ]
    print(">>> Removed builds with ALL mains of the same ability")
    # Replacing all builds with no specified game modes to be generic
    # --- Assistance from ChatGPT ------------------------------------------
    builds_df_edit_3 = builds_df_edit_2.copy()  # create a copy
    # Convert the strings that represent lists to actual lists
    builds_df_edit_3['game_modes'] = builds_df_edit_3['game_modes'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) else x
    )
    # List of all game modes
    all_modes = ['Splat Zones', 'Tower Control',
                 'Rainmaker', 'Clam Blitz', 'Turf War']
    # Replace rows where 'game_modes' is ['NO MODES LISTED'] to all_modes
    builds_df_edit_3['game_modes'] = builds_df_edit_3['game_modes'].apply(
        lambda x: all_modes if x == ['NO MODES LISTED'] else x
    )
    # -----------------------------------------------------------------------
    print(">>> Made Builds with no specified game modes generic\x1b[0m")
    print("Original data frame: \x1b[33m" +
          str(builds_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(builds_df.shape[1]) + " columns\x1b[0m")
    print("Cleaned data frame: \x1b[33m" +
          str(builds_df_edit_3.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(builds_df_edit_3.shape[1]) + " columns\x1b[0m")
    print("\x1b[0m" + "-" * 80)
    return builds_df_edit_3


# enrich builds by adding the weapon details from the weapon df
def enrich_builds_df(builds_df, weapons_df):
    print("\x1b[34mEnriching \x1b[36mbuilds dataframe...")
    builds_df_2 = builds_df.copy()
    builds_df_2 = pd.merge(
        builds_df, weapons_df, left_on='Weapon_name', right_on='Name',
        how='left')
    builds_df_2 = builds_df_2.drop(
        ['Name'], axis=1)
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Added weapon details")
    # rename columns also
    builds_df_2 = builds_df_2.rename(columns={'Weapon_name': 'Weapon_Name'})
    builds_df_2 = builds_df_2.rename(columns={'game_modes': 'Game_Modes'})
    builds_df_2 = builds_df_2.rename(columns={'Sub': 'Sub_Weapon'})
    builds_df_2 = builds_df_2.rename(columns={'Special': 'Special_Weapon'})
    print(">>> Renamed multiple columns\x1b[0m")
    print("Enriched data frame: \x1b[33m" +
          str(builds_df_2.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(builds_df_2.shape[1]) + " columns\x1b[0m")
    print("\x1b[0m" + "-" * 80)
    return builds_df_2


# function to create aggregate dfs from builds df
def aggregate_builds_df(builds_df):
    print("\x1b[34mAggregating \x1b[36mbuilds dataframe...")
    # call this function to create 2 aggregate dfs
    (AP_builds_df, Ability_builds_df) = Ability_dataframes(builds_df)
    print("\x1b[0m" + "-" * 80)
    print(
        "\x1b[35m>>> Created a version of the builds data frame "
        "that has lists for mains and subs")
    print("\x1b[35m>>> Removed old main and sub ability columns")
    print("\x1b[0mbuilds data frame with ability lists: \x1b[33m" +
          str(Ability_builds_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(Ability_builds_df.shape[1]) + " columns\x1b[0m")
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created a version of the builds data frame"
          "that has columns for each ability")
    print("\x1b[35m>>> Removed old main and sub ability columns")
    print("\x1b[0mbuilds data frame with ability columns: \x1b[33m" +
          str(AP_builds_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(AP_builds_df.shape[1]) + " columns\x1b[0m")
    # call this function to create 5 aggregate dfs
    (ALL_mean_df, WEAPON_mean_df,
     CLASS_mean_df, SUB_mean_df,
     SPECIAL_mean_df) = Aggregate_Means(AP_builds_df)
    # -----------
    # call function to create mode aggregate dfs
    ALL_modes_df, WEAPON_modes_df = Aggregate_modes_df(builds_df)
    # return all 9 created dfs
    return (AP_builds_df, Ability_builds_df, ALL_mean_df, WEAPON_mean_df,
            CLASS_mean_df, SUB_mean_df, SPECIAL_mean_df,
            ALL_modes_df, WEAPON_modes_df)


# want to observe the game modes suggested for different main weapons
# to do create some new dfs
def Aggregate_modes_df(builds_df):
    # Create the modes df
    modes_df = Calculate_Modes(builds_df)
    # Create 2 dfs for mode totals
    All_builds_modes_df, Weapon_builds_modes_df = total_modes(modes_df)
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created a df for game modes summary across all builds")
    print("\x1b[0mMode Totals data frame: \x1b[33m" +
          str(All_builds_modes_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(All_builds_modes_df.shape[1]) + " columns\x1b[0m")
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created a df for game modes summary for each weapon")
    print("\x1b[0mWeapon Mode Totals data frame: \x1b[33m" +
          str(Weapon_builds_modes_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(Weapon_builds_modes_df.shape[1]) + " columns\x1b[0m")
    print("\x1b[0m" + "-" * 80)
    return All_builds_modes_df, Weapon_builds_modes_df


# Calculate totals of each mode column
# for all builds and also
# group by weapon
def total_modes(modes_df):
    WEAPONS_df = modes_df.copy()
    # drop columns
    All_df = modes_df.drop(['Weapon_Name', 'Game_Modes'], axis=1)
    # calc totals over all builds
    ALL_totals = All_df.sum(axis=0)
    # convert to df
    ALL_totals_df = ALL_totals.to_frame().T
    # -----------------
    # group by weapon name and calc totals for each
    WEAPON_totals_df = WEAPONS_df.groupby('Weapon_Name').sum(
        numeric_only=True
    ).reset_index()
    return ALL_totals_df, WEAPON_totals_df


# Create a new dataframe with new calculated columns
# for game modes
def Calculate_Modes(builds_df):
    # Only include needed columns, drop the rest
    modes_df = builds_df.loc[:, ['Weapon_Name', 'Game_Modes']]
    # define new columns
    mode_columns_1 = ['Turf_War_Only', 'Splat_Zones_Only',
                      'Rainmaker_Only', 'Tower_Control_Only',
                      'Clam_Blitz_Only', 'Not_Singular_Mode']
    mode_columns_2 = ['Turf_War_YES', 'Turf_War_NO',
                      'Splat_Zones_YES', 'Splat_Zones_NO',
                      'Rainmaker_YES', 'Rainmaker_NO',
                      'Tower_Control_YES', 'Tower_Control_NO',
                      'Clam_Blitz_YES', 'Clam_Blitz_NO']
    mode_columns_3 = ['1_modes', '2_modes', '3_modes',
                      '4_modes', '5_modes', 'Total']
    # set all to 0 to start
    modes_df[mode_columns_1] = 0
    modes_df[mode_columns_2] = 0
    modes_df[mode_columns_3] = 0
    # list of possible values that Game_Modes lists can have
    modes = ['Turf War', 'Splat Zones', 'Tower Control',
             'Rainmaker', 'Clam Blitz']
    # loop through all rows
    for idx, row in modes_df.iterrows():
        # find the list of game modes
        game_modes = row['Game_Modes']
        # add 1 to overall total for each build
        modes_df.at[idx, 'Total'] = 1
        # Onto calculating the numbers in each column
        # do mode_columns_2 first ---------------------------------
        # loop through all the possible modes
        for mode in modes:
            # formatting to match column names
            mode_format = mode.replace(" ", "_")
            # check if the game mode is included
            if mode in game_modes:
                # if yes update the respective YES column
                column = mode_format + "_YES"
                modes_df.at[idx, column] = 1
            else:
                # if no update the respective NO column
                column = mode_format + "_NO"
                modes_df.at[idx, column] = 1
        # do mode_columns_3 next ----------------------------------
        # check length of the list of modes
        number_of_modes = len(game_modes)
        # find the column for that length
        numb_column = str(number_of_modes) + '_modes'
        # update it
        modes_df.at[idx, numb_column] = 1
        # do mode_columns_1 next ----------------------------------
        # check if the list length is 1
        if number_of_modes == 1:
            # if yes find out what mode it is
            for mode in modes:
                mode_format = mode.replace(" ", "_")
                # check if its the right mode
                if mode in game_modes:
                    # if yes update the mode's Only column
                    column = mode_format + "_Only"
                    modes_df.at[idx, column] = 1
                    break
        # if any other length than 1
        else:
            # update this column instead
            modes_df.at[idx, 'Not_Singular_Mode'] = 1
    # return the now filled in df
    return modes_df


# Creating the following aggregate dfs
# 1. A df of the means for all builds
# 2. A df of the means for each main weapon's builds
# 3. A df of the means for each weapon class's builds
# 4. A df of the means for each sub weapon's builds
# 5. A df of the means for each special weapon's builds
def Aggregate_Means(AP_builds_df):
    # 1. ALL ------------------------------------------------------------
    ALL_mean_df = All_means(AP_builds_df)
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created dataframe for means across all builds")
    print("\x1b[0mAll builds Means data frame: \x1b[33m" +
          str(ALL_mean_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(ALL_mean_df.shape[1]) + " columns\x1b[0m")
    # 2. WEAPON ---------------------------------------------------------
    WEAPON_mean_df = Weapon_means(AP_builds_df)
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created dataframe for means for each weapon's builds")
    print("\x1b[0mWeapon builds Means data frame: \x1b[33m" +
          str(WEAPON_mean_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(WEAPON_mean_df.shape[1]) + " columns\x1b[0m")
    # 3. CLASS ----------------------------------------------------------
    CLASS_mean_df = class_means(AP_builds_df)
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created dataframe for means"
          "for each weapon class's builds")
    print("\x1b[0mWeapon class builds Means data frame: \x1b[33m" +
          str(CLASS_mean_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(CLASS_mean_df.shape[1]) + " columns\x1b[0m")
    # 4. SUB ------------------------------------------------------------
    SUB_mean_df = sub_means(AP_builds_df)
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created dataframe for means"
          "for each sub weapon's builds")
    print("\x1b[0mSub weapon builds Means data frame: \x1b[33m" +
          str(SUB_mean_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(SUB_mean_df.shape[1]) + " columns\x1b[0m")
    # 5. SPECIAL --------------------------------------------------------
    SPECIAL_mean_df = special_means(AP_builds_df)
    print("\x1b[0m" + "-" * 80)
    print("\x1b[35m>>> Created dataframe for means"
          "for each special weapon's builds")
    print("\x1b[0mSpecial weapon builds Means data frame: \x1b[33m" +
          str(SPECIAL_mean_df.shape[0]) +
          " rows \x1b[0mand \x1b[33m"
          + str(SPECIAL_mean_df.shape[1]) + " columns\x1b[0m")
    # return all the dfs
    return (ALL_mean_df,
            WEAPON_mean_df, CLASS_mean_df,
            SUB_mean_df, SPECIAL_mean_df)


# function to return the mean values for builds grouped by Main Weapon
def Weapon_means(AP_builds_df):
    # create a copy to work with
    WEAPON_mean_df = AP_builds_df.copy()
    # drop columns that are not needed (not related to the Main)
    WEAPON_mean_df = WEAPON_mean_df.drop(
        ['Game_Modes', 'Main_Abilities', 'Sub_Abilities'],
        axis=1
    )
    # Find the non numeric columns of the df
    WEAPON_group_df = WEAPON_mean_df.select_dtypes(exclude=['number'])
    # group by Main Weapon
    # by taking the first row values found for each Main
    WEAPON_group_df = WEAPON_group_df.groupby('Weapon_Name').first()
    # group by Main Weapon
    # and find the means of numeric columns
    WEAPON_mean_df = (
        WEAPON_mean_df.groupby('Weapon_Name')
        .mean(numeric_only=True)
    )
    # group by Main Weapon
    # and calculate how many builds for each Main
    Group_Counts_df = (
        AP_builds_df.groupby('Weapon_Name')
        .size()
        .reset_index(name='Build_Count')
    )
    # combine the means with the non numeric values
    WEAPON_mean_df_complete = pd.merge(
        WEAPON_group_df,
        WEAPON_mean_df,
        on='Weapon_Name'
    )
    # combine this with the build counts
    WEAPON_mean_df_complete_2 = pd.merge(
        WEAPON_mean_df_complete,
        Group_Counts_df,
        on='Weapon_Name'
    )
    # return the complete df
    return WEAPON_mean_df_complete_2


# function to return the mean values for builds grouped by class
def class_means(AP_builds_df):
    # create a copy to work with
    CLASS_mean_df = AP_builds_df.copy()
    # drop columns that are not needed (not related to the class)
    CLASS_mean_df = CLASS_mean_df.drop(
        [
            'Game_Modes', 'Main_Abilities', 'Sub_Abilities', 'Sub_Weapon',
            'Weapon_Img', 'Sub_Img', 'Special_Img', 'Special_Weapon',
            'Weapon_Name'
        ],
        axis=1
    )
    # Find the non numeric columns of the df
    CLASS_group_df = CLASS_mean_df.select_dtypes(exclude=['number'])
    # group by class
    # by taking the first row values found for each class
    CLASS_group_df = CLASS_group_df.groupby('Class').first()
    # group by class
    # and calculate how many builds for each class
    CLASS_mean_df = CLASS_mean_df.groupby('Class').mean(numeric_only=True)
    # group by class
    # and calculate how many builds for each class
    Group_Counts_df = (
        AP_builds_df.groupby('Class')
        .size()
        .reset_index(name='Build_Count')
    )
    # combine the means with the non numeric values
    CLASS_mean_df_complete = pd.merge(
        CLASS_group_df,
        CLASS_mean_df,
        on='Class')
    # combine this with the build counts
    CLASS_mean_df_complete_2 = pd.merge(
        CLASS_mean_df_complete,
        Group_Counts_df,
        on='Class')
    # return the complete df
    return CLASS_mean_df_complete_2


# function to return the mean values for builds grouped by sub weapon
def sub_means(AP_builds_df):
    # create a copy to work with
    SUB_mean_df = AP_builds_df.copy()
    # drop columns that are not needed (not related to the sub)
    SUB_mean_df = SUB_mean_df.drop(
        [
            'Game_Modes', 'Main_Abilities', 'Sub_Abilities',
            'Class', 'Weapon_Img', 'Class_Img',
            'Special_Img', 'Special_Weapon', 'Weapon_Name'
        ],
        axis=1
    )
    # Find the non numeric columns of the df
    SUB_group_df = SUB_mean_df.select_dtypes(exclude=['number'])
    # group by sub Weapon
    # by taking the first row values found for each sub
    SUB_group_df = SUB_group_df.groupby('Sub_Weapon').first()
    # group by sub Weapon
    # and calculate how many builds for each sub
    SUB_mean_df = SUB_mean_df.groupby('Sub_Weapon').mean(numeric_only=True)
    # group by sub Weapon
    # and calculate how many builds for each sub
    Group_Counts_df = (
        AP_builds_df.groupby('Sub_Weapon')
        .size()
        .reset_index(name='Build_Count')
    )
    # combine the means with the non numeric values
    SUB_mean_df_complete = pd.merge(SUB_group_df, SUB_mean_df, on='Sub_Weapon')
    # combine this with the build counts
    SUB_mean_df_complete_2 = pd.merge(
        SUB_mean_df_complete,
        Group_Counts_df,
        on='Sub_Weapon'
    )
    # return the complete df
    return SUB_mean_df_complete_2


# function to return the mean values for builds grouped by special weapon
def special_means(AP_builds_df):
    # create a copy to work with
    SPECIAL_mean_df = AP_builds_df.copy()
    # drop columns that are not needed (not related to the special)
    SPECIAL_mean_df = SPECIAL_mean_df.drop(
        [
            'Game_Modes', 'Main_Abilities', 'Sub_Abilities',
            'Class', 'Weapon_Img', 'Class_Img',
            'Sub_Img', 'Sub_Weapon', 'Weapon_Name'
        ],
        axis=1
    )
    # Find the non numeric columns of the df
    SPECIAL_group_df = SPECIAL_mean_df.select_dtypes(exclude=['number'])
    # group by Special Weapon
    # by taking the first row values found for each special
    SPECIAL_group_df = SPECIAL_group_df.groupby('Special_Weapon').first()
    # group by special Weapon
    # and find the means of numeric columns
    SPECIAL_mean_df = (
        SPECIAL_mean_df.groupby('Special_Weapon')
        .mean(numeric_only=True)
    )
    # group by special Weapon
    # and calculate how many builds for each special
    Group_Counts_df = (
        AP_builds_df.groupby('Special_Weapon')
        .size()
        .reset_index(name='Build_Count')
    )
    # combine the means with the non numeric values
    SPECIAL_mean_df_complete = pd.merge(
        SPECIAL_group_df,
        SPECIAL_mean_df,
        on='Special_Weapon'
    )
    # combine this with the build counts
    SPECIAL_mean_df_complete_2 = pd.merge(
        SPECIAL_mean_df_complete,
        Group_Counts_df,
        on='Special_Weapon'
    )
    # return the complete df
    return SPECIAL_mean_df_complete_2


# function to return the mean values across ALL builds
def All_means(AP_builds_df):
    # create a copy tow work with
    ALL_mean_df = AP_builds_df.copy()
    # select only numeric columns
    ALL_mean_df = ALL_mean_df.select_dtypes(include='number')
    # Create a dataframe from the means
    # Transpose so we have the same column format
    ALL_mean_df = pd.DataFrame(ALL_mean_df.mean()).T
    # Count how many builds there were in the orig df
    # Add this to end of the means df
    ALL_mean_df['Builds_Count'] = AP_builds_df.shape[0]
    # return the new df
    return ALL_mean_df


# transform the builds dataframe to create
# 1. a builds dataframe with a columns for list of subs and mains
# 2. with (1) a builds dataframe with each ability being its own row
#    with a numeric value for the amount the build uses each
def Ability_dataframes(builds_df):
    # create a copy of the orig builds df
    Ability_builds_df = builds_df.copy()
    # combine Mains to a list in a new column
    Ability_builds_df['Main_Abilities'] = Ability_builds_df[
        ['Main_1', 'Main_2', 'Main_3']
        ].agg(list, axis=1)
    # combine Subs to a list in a new column
    Ability_builds_df['Sub_Abilities'] = Ability_builds_df[
        ['Sub_1', 'Sub_2', 'Sub_3', 'Sub_4', 'Sub_5', 'Sub_6',
         'Sub_7', 'Sub_8', 'Sub_9']
        ].agg(list, axis=1)
    # create a copy of this for doing AP calculations
    AP_builds_df = Ability_builds_df.copy()
    # From list of mains and subs create columns for each ability
    # for trackable abilities calculate APs (Ability Points)
    # for non trackable just use 1s or 0s
    AP_builds_df = AP_calculation(AP_builds_df, builds_df)
    # drop columns
    Ability_builds_df = Ability_builds_df.drop(
        [
            'Main_1', 'Main_2', 'Main_3',
            'Sub_1', 'Sub_2', 'Sub_3',
            'Sub_4', 'Sub_5', 'Sub_6',
            'Sub_7', 'Sub_8', 'Sub_9'
        ],
        axis=1
    )
    # print("Ability_builds_df")
    # display(Ability_builds_df)
    # return both dataframes with new columns
    return AP_builds_df, Ability_builds_df


# Find and return ability lists
def Ability_Lists(builds_df):
    # Find all sub abilites (can be tracked)
    Track_abilities = builds_df['Sub_1'].unique()
    # Find all possible abilites
    All_abilities = pd.concat([
        builds_df['Main_1'],
        builds_df['Main_2'],
        builds_df['Main_3']
    ])
    All_abilities = All_abilities.unique()
    # convert to sets
    Track_abilities = set(Track_abilities)
    All_abilities = set(All_abilities)
    # so we can find the difference
    # to find abilities that are not subs only mains
    Non_Track_abilities = All_abilities.difference(Track_abilities)
    # return both lists
    return list(Track_abilities), list(Non_Track_abilities)


def AP_calculation(AP_builds_df, builds_df):
    # call a function to find both trackable with APs abilities
    # and those that can't be
    Track_abilities, Non_Track_abilities = Ability_Lists(builds_df)
    # add new columns for all possible abilities, set to 0 for now
    AP_builds_df[Non_Track_abilities] = 0
    AP_builds_df[Track_abilities] = 0
    # drop columns we don't need
    AP_builds_df = AP_builds_df.drop(
        [
            'Main_1', 'Main_2', 'Main_3',
            'Sub_1', 'Sub_2', 'Sub_3',
            'Sub_4', 'Sub_5', 'Sub_6',
            'Sub_7', 'Sub_8', 'Sub_9'
        ],
        axis=1
    )
    # loop through each trackable ability
    for ability in Track_abilities:
        # find the column for that ability
        # and update it with a +10 for every main of that ability found
        AP_builds_df[ability] += AP_builds_df['Main_Abilities'].apply(
            lambda x: 10 * x.count(ability)
        )
    # loop through each non trackable ability
    for ability in Non_Track_abilities:
        # find the column for that ability
        # and update it with a 1 if a main of that ability is found
        AP_builds_df[ability] += AP_builds_df['Main_Abilities'].apply(
            lambda x: 1 * x.count(ability)
        )
    # loop through each trackable ability
    for ability in Track_abilities:
        # find the column for that ability
        # and update it with a +3 if a sub of that ability is found
        # x represents an element in the Sub_abilities column
        # (so count how many there are and multiply by 3 to get total points)
        AP_builds_df[ability] += AP_builds_df['Sub_Abilities'].apply(
            lambda x: 3 * x.count(ability)
        )
    # return this dataframe
    return AP_builds_df
