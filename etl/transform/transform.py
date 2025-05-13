from etl.transform.transform_weapons import transform_weapons_df
from etl.transform.transform_builds import transform_builds_df


# function to do all dataframe transformations
def transform_data():
    # transform weapons dataframe
    weapons_df = transform_weapons_df("data")
    print("\n\n")
    build_df_tuple = transform_builds_df(weapons_df, "data")
    # print(weapons_df)
