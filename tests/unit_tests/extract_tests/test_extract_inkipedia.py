from bs4 import BeautifulSoup
# import requests
import time
import pandas as pd

import pytest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
import requests
from unittest.mock import patch
from requests.exceptions import Timeout, RequestException

from etl.extract.url_request import make_request
from etl.extract.extract_inkipedia import extract_inkipedia
from etl.extract.extract_inkipedia import scrape_weapon_details
from etl.extract.extract_inkipedia import scrape_row
from etl.extract.extract_inkipedia import reshaping_weapon_details


# START TESTING extract_inkepedia()

# test if def extract_inkipedia() returns a dataframe
@patch('etl.extract.extract_inkipedia.extract_weapon_details')
def test_def_extract_inkipedia(mock_extract_weapons):
    # Arrange
    # An empty array as an example of an input
    mock_extract_weapons.return_value = pd.DataFrame({'testing' : []})
    # Action
    actual_output = extract_inkipedia() # what the function actually returns
    # Assert
    assert isinstance(actual_output, pd.DataFrame) # check if it returns a dataframe
    
# FINISHED TESTING extract_inkepedia()

# START TESTING extract_weapon_details()
    

# FINISHED TESTING extract_weapon_details()


# START TESTING scrape_weapon_details():

# testing if function returns a list
@patch('etl.extract.extract_inkipedia.scrape_row')
def test_scrape_weapon_details(mock_scrape_row):
    # Arrange
    mock_soup = Mock() # mock soup
    # when find_all is called return this generic list to represent the html which is usually received
    mock_soup.find_all.return_value = ['html_1', 'html_2','html_2']
    # --- Assistance from ChatGPT -----------------
    # simulate the adding of elements to the overall list as scrape row is called in the loop
    mock_scrape_row.side_effect = [
        ['details0', 'details1'],
        ['details0', 'details1','details2', 'details3'],
        ['details0', 'details1','details2', 'details3','details4', 'details5']
    ]
    # ----------------------------------------------
    # what we expect to be returned
    expected_output = ['details0', 'details1','details2', 'details3','details4', 'details5']
    # Action
    actual_outcome = scrape_weapon_details(mock_soup) # what is actually returned
    # Assert
    assert actual_outcome == expected_output # compare
    
# FINISHED TESTING scrape_weapon_details():

# START TESTING scrape_weapon_details():

def test_scrape_row():
    # Arrange
    # a shortened ver of an example of html for a row
    ex_html = '<tr><td>Sploosh-o-matic</td><td>0</td><td>Curling Bomb</td><td>Ultra Stamp</td></tr>'
    ex_html = BeautifulSoup(ex_html, 'html.parser').tr # convert to a html tag object
    mock_row = ex_html # this will be used to simulate a real row
    # we expect the function to correctly retrieve the data in td tags
    expected_output = ['Sploosh-o-matic','0','Curling Bomb','Ultra Stamp']
    # Action
    actual_output = scrape_row(mock_row, []) # what is actually returned
    # Assert
    assert expected_output == actual_output # check if same

# FINISHED TESTING scrape_weapon_details():


# START TESTING reshaping_weapon_details()

def test_reshaping_weapon_details():
    # Arrange
    # example of a 1d array
    mock_list = ['1','2','3','4','5','6','7','8','9','10',
                 '1','2','3','4','5','6','7','8','9','10',
                 '1','2','3','4','5','6','7','8','9','10']
    # we  want to convert to 2d by grouping every 10 elements
    expected_output = [['1','2','3','4','5','6','7','8','9','10'],
                        ['1','2','3','4','5','6','7','8','9','10'],
                        ['1','2','3','4','5','6','7','8','9','10']]
    # Action
    actual_output = reshaping_weapon_details(mock_list) # what the funtion returns
    # Assert
    assert expected_output == actual_output # check if same

# FINISHED TESTING reshaping_weapon_details()
