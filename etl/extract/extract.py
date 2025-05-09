from etl.extract.extract_sendou_builds import extract_sendou_data
from etl.extract.extract_inkipedia import extract_inkipedia

# function extract all data from sendou and inkepedia
def extract_data():
    builds_df = extract_sendou_data()
    weapons_df = extract_inkipedia()
    return builds_df,weapons_df
