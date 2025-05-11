from etl.extract.extract_sendou_builds import extract_sendou_data
from etl.extract.extract_inkipedia import extract_inkipedia
from etl.extract.extract_inkipedia_images import extract_main_weapon_images
from etl.extract.extract_ink_ability_images import extract_ability_images
from etl.extract.extract_ink_special_images import extract_specials_images


# function extract all data from sendou and inkepedia
def extract_data():
    builds_df = extract_sendou_data()
    weapons_df = extract_inkipedia()
    w_names = weapons_df['Name']
    main_weapon_images = extract_main_weapon_images(w_names)
    ability_images = extract_ability_images(builds_df)
    special_images = extract_specials_images(weapons_df)
    # print(main_weapon_images)
    return builds_df, weapons_df
