
import sys

from config.env_config import setup_env
from etl.extract.extract import extract_data
from etl.extract.df_and_csv import extract_to_csv
from etl.transform.transform import transform_data
from etl.load.load import load_data

DO_EXTRACT = True


def main():
    print("\n")
    print("\033[1;32m[INFO] Starting the ETL process...\033[0m")
    # Extract -----------------------------------------------------------
    if DO_EXTRACT:
        print("\n[INFO] BEGIN EXTRACTING")
        (
            builds_df, weapons_df, ability_img_df,
            special_img_df, sub_img_df, weapon_img_df, class_img_df
        ) = extract_data()
        print("\n[INFO] FINISHED EXTRACTING\n")
        extract_to_csv([
            builds_df, weapons_df, ability_img_df,
            special_img_df, sub_img_df, weapon_img_df, class_img_df
        ])
    else:
        print("\nSkipped extraction")
    # Transform ----------------------------------------------------------
    print("\n[INFO] BEGIN TRANSFORMING\n")
    weapons_df, build_df_tuple = transform_data()
    all_dfs_tuple = (weapons_df, *build_df_tuple)
    print("\n[INFO] FINISHED TRANSFORMING\n")
    # Load ---------------------------------------------------------------
    print("\n[INFO] BEGIN LOADING\n")
    load_data(all_dfs_tuple)
    print("\n[INFO] FINISHED LOADING\n")
    print("\033[1;32m[INFO] ETL process completed successfully.\033[0m")
    print("\n")
    # run_env_setup()

    # print(
    #       f"ETL pipeline run successfully in "
    #       f'{os.getenv("ENV", "error")} environment!'
    #   )


def run_env_setup():
    print("\n")
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


if __name__ == "__main__":
    main()
