from etl.transform.transform_weapons import transform_weapons_df


# function to do all dataframe transformations
def transform_data():
    # transform weapons dataframe
    weapons_df = transform_weapons_df("data")
    # print(weapons_df)
