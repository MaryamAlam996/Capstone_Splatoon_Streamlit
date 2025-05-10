from etl.extract.extract_sendou_builds import extract_sendou_data
from etl.extract.extract_inkipedia import extract_inkipedia
from etl.extract.extract_inkipedia_images import extract_main_weapon_images


# function extract all data from sendou and inkepedia
def extract_data():
    builds_df = extract_sendou_data()
    weapons_df = extract_inkipedia()
    w_names = weapons_df['Name']
    main_weapon_images = extract_main_weapon_images(w_names)
    print(main_weapon_images)
    return builds_df, weapons_df
