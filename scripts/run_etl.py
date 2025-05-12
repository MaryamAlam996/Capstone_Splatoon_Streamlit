import os
import sys

from config.env_config import setup_env
from etl.extract.extract import extract_data
from etl.extract.df_and_csv import extract_to_csv

DO_EXTRACT = True


def main():
    if DO_EXTRACT:
        print("\nBEGIN EXTRACTING:")
        (
            builds_df, weapons_df, ability_img_df,
            special_img_df, sub_img_df, weapon_img_df, class_img_df
        ) = extract_data()
        print("\nFINISHED EXTRACTING:\n")
        extract_to_csv([
            builds_df, weapons_df, ability_img_df,
            special_img_df, sub_img_df, weapon_img_df, class_img_df
        ])
    else:
        print("\nSkipped extraction")

    run_env_setup()

    print(
          f"ETL pipeline run successfully in "
          f'{os.getenv("ENV", "error")} environment!'
      )


def run_env_setup():
    print("\n")
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


if __name__ == "__main__":
    main()
