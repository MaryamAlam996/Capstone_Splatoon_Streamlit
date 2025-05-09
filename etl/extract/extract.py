from etl.extract.extract_sendou_builds import extract_sendou_data


# function extract all data from sendou and inkepedia
def extract_data():
    builds_df = extract_sendou_data()
    return builds_df
