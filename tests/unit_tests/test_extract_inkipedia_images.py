from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# Testing-related imports
import pytest
from unittest.mock import patch, Mock
from requests.exceptions import Timeout, RequestException

from etl.extract.extract_inkipedia_images import extract_main_weapon_images
from etl.extract.extract_inkipedia_images import find_all_weapon_pages
from etl.extract.extract_inkipedia_images import find_weapon_path
from etl.extract.extract_inkipedia_images import fix_names
from etl.extract.extract_inkipedia_images import find_all_weapon_urls
from etl.extract.extract_inkipedia_images import find_all_images
from etl.extract.extract_inkipedia_images import start_session


# START TESTING extract_main_weapon_images()





# FINISH TESTING extract_main_weapon_images()




