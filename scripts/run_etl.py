import os
import sys

from config.env_config import setup_env
from etl.extract.extract import extract_data


def main():
    print("hello!")
    builds_df, weapons_df = extract_data()
    # print('Data Frame of builds:')
    # print(builds_df)
    # print('Data Frame of weapon details:')
    # print(weapons_df)
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
