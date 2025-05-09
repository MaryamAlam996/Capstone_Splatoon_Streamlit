import pytest
from unittest.mock import patch, Mock, MagicMock
from bs4 import BeautifulSoup
import requests
from unittest.mock import patch
from requests.exceptions import Timeout, RequestException
from bs4 import BeautifulSoup
import pandas as pd

from etl.extract.extract_sendou_builds import make_request
from etl.extract.extract_sendou_builds import weapon_build_paths
from etl.extract.extract_sendou_builds import search_for_build_path
from etl.extract.extract_sendou_builds import add_to_list
from etl.extract.extract_sendou_builds import scrape_a_build
from etl.extract.extract_sendou_builds import scrape_all_builds
from etl.extract.extract_sendou_builds import extract_modes
from etl.extract.extract_sendou_builds import extract_abilities
from etl.extract.extract_sendou_builds import create_weapon_build_df

# START TESTING search_for_build_path()

# testing the handling of links with no href
def test_search_for_build_path_if_href_none():
    # Arrange
    mock_link = Mock() # Mock object to simulate a real link
    mock_link.get.return_value = None # When mock_link.get('href') is called return None as there is no href
    expected_output = (None, None) # We expect to see None values returned for both path 
                                   # and weapon_name (to indicate skipping this link in the list)
                                   
    # Action
    actual_output = search_for_build_path(mock_link) # What the function actually returns
    
    # Assert
    assert actual_output == expected_output # check to see if they are the same

# testing the handling of links with a href that is not for a builds page
def test_search_for_build_path_if_href_is_not_for_build():
    # Arrange
    mock_link = Mock() # Mock object to simulate a real link
    mock_link.get.return_value = '/not-builds/jet-squelcher' # href is not /builds/jet-squelcher so should be skipped
    expected_output = (None, None) # We expect to see None values returned for both path
                                   # and weapon_name (to indicate skipping this link in the list) 
                                   
    # Action
    actual_output = search_for_build_path(mock_link) # What the function actually returns
    
    # Assert
    assert actual_output == expected_output # check to see if they are the same
 
 # Parameters we will use to test multiple example scenarios
@pytest.mark.parametrize("href, expected_url, expected_weapon_name", [
    ('/builds/jet-squelcher', 'https://sendou.ink/builds/jet-squelcher', 'Jet Squelcher'),
    ('/builds/52-gal', 'https://sendou.ink/builds/52-gal', '.52 Gal'),
    ('/builds/n-zap-89', 'https://sendou.ink/builds/n-zap-89', "N-ZAP '89")
])

# testing to see if the correct URL and weapon name are returned per each href
# using the above parameters to test multiple examples of valid hrefs
def test_search_for_build_path_if_href_is_for_build(href, expected_url, expected_weapon_name):

    # Arrange
    mock_link = Mock() # Mock object to simulate a real link
    mock_link.get.return_value = href # testing each valid href
    mock_link.get_text.return_value = expected_weapon_name # returns weapon name for the href
    expected_output = (expected_url, expected_weapon_name) # expected result of correct url and name
    
    # Action
    actual_output = search_for_build_path(mock_link) # What the function actually returns
    
    # Assert
    assert actual_output == expected_output # check to see if they are the same
    
@pytest.mark.parametrize("href, expected_url, expected_weapon_name", [
    ('/builds/jet-squelcher', None, None),
    ('/builds/52-gal', None, None),
    ('/builds/n-zap-89', None, None)
])
 
# testing to see if None values are returned if the href.get_text is none
# using the above parameters to test multiple examples of valid hrefs
def test_search_for_build_path_if_href_is_for_build_text_none(href, expected_url, expected_weapon_name):
    # Arrange
    mock_link = Mock() # Mock object to simulate a real link
    mock_link.get.return_value = href # testing each valid href
    mock_link.get_text.return_value = expected_weapon_name # returns None for the name for each href
    expected_output = (expected_url, expected_weapon_name) # expected result of correct url and name
    
    # Action
    actual_output = search_for_build_path(mock_link) # What the function actually returns
    
    # Assert
    assert actual_output == expected_output # check to see if they are the same
    

# FINISHED TESTING search_for_build_path()


# START TESTING weapon_build_paths()


# testing that when number of paths and weapon names are equal 
# it returns both of these
# INSERT TEST HERE


# FINISHED TESTING weapon_build_paths()


# START TESTING add_to_list()

# testing to see if the function appends to the list if element not none
def test_add_to_list_not_none():
    # Arrange
    the_list = ['existing_elm'] # example of a list
    the_elm = 'not_null_elm' # example of a valid element we want to add
    expected_output = ['existing_elm', 'not_null_elm'] # what the list should look like
    # Action
    actual_output = add_to_list(the_list, the_elm) # the list the function actually returns
    # Assert
    assert actual_output == expected_output # check to see if they are the same
    
# testing to see if the function does not append to the list if the element is none
def test_add_to_list_none():
    # Arrange
    the_list = ['existing_elm'] # example of a list
    the_elm = None # example of a invalid element we don't want to add
    expected_output = ['existing_elm'] # what the list should look like
    # Action
    actual_output = add_to_list(the_list, the_elm) # the list the function actually returns
    # Assert
    assert actual_output == expected_output # check to see if they are the same

# END TESTING add_to_list()

# START TESTING scrape_a_build()

# Test to check if scrape_a_build returns two lists
# patch is used to replace the return value of these functions
@patch('etl.extract.extract_sendou_builds.extract_modes')
@patch('etl.extract.extract_sendou_builds.extract_abilities')   
def test_scrape_a_build(mock_extract_modes, mock_extract_abilities):
    # Arrange
    mock_build = Mock() # mock object
    # When calling the function extract_modes return this!
    mock_extract_modes.return_value = ['item_3', 'item_4'] 
    # When calling the function extract_abilities return this!
    mock_extract_abilities.return_value = ['item_1', 'item_2'] 
    expected_output = (['item_3', 'item_4'], ['item_1', 'item_2']) # what the lists should look like
    # Action
    actual_output = scrape_a_build(mock_build) # the lists the function actually return
    # Assert
    assert actual_output == expected_output # check to see if they are the same
    
# FINISHED TESTING scrape_a_build()

# START TESTING extract_abilities()

# Test to check if extract_abilities returns a list
def test_extract_abilities():
    # Arrange
    # an example of an ability (as html)
    ex_ability_html = '<div class="build__ability readonly"><img alt="Opening Gambit" src="/static-assets/img/abilities/OG.png"/></div>'
    # --- Assistance from ChatGPT ---
    ex_ability = BeautifulSoup(ex_ability_html, 'html.parser').div  # Create a Tag object
    mock_build = Mock()
    # When finding the abilities use this instead
    mock_build.find_all.return_value = [ex_ability, ex_ability] 
    # --------------------------------
    expected_output = ['Opening Gambit', 'Opening Gambit'] # what the list should look like
    # Action
    actual_output = extract_abilities(mock_build) # the list the function actually return
    # Assert
    assert actual_output == expected_output # check to see if they are the same

# END TESTING extract_abilities()

# START TESTING extract_modes()

# Test to check if extract_modes() returns a list when modes is found
def test_extract_modes():
    # Arrange
    # an example of modes (as html)
    ex_modes_html = '<div class="build__modes"><img alt="Splat Zones" src="/static-assets/img/modes/SZ.png"/><img alt="Tower Control" src="/static-assets/img/modes/TC.png"/><img alt="Rainmaker" src="/static-assets/img/modes/RM.png"/><img alt="Clam Blitz" src="/static-assets/img/modes/CB.png"/></div>'
    # --- Assistance from ChatGPT ---
    ex_modes = BeautifulSoup(ex_modes_html, 'html.parser').div  # Create a Tag object
    mock_build = Mock()
    # When finding the mode list use this instead
    mock_build.find.return_value = ex_modes
    # --------------------------------
    expected_output = ['Splat Zones', 'Tower Control', 'Rainmaker','Clam Blitz'] # what the list should look like
    # Action
    actual_output = extract_modes(mock_build) # the list the function actually returns
    # Assert
    assert actual_output == expected_output # check to see if they are the same
     
# Test to check if extract_modes() returns ['NO MODES LISTED'] when modes is None
def test_extract_modes_none():
    # Arrange
    # --- Assistance from ChatGPT ---
    mock_build = Mock()
    # When finding the mode list use this (None)
    mock_build.find.return_value = None  
    # --------------------------------
    expected_output = ['NO MODES LISTED'] # what the list should look like
    # Action
    actual_output = extract_modes(mock_build) # the list the function actually returns
    # Assert
    assert actual_output == expected_output # check to see if they are the same

# END TESTING extract_modes()

# START TESTING scrape_all_builds()

# --- Assistance from ChatGPT to help write this function ---
# testing to see if this returns a dataframe where each row is a build
@patch('etl.extract.extract_sendou_builds.scrape_a_build')
def test_scrape_all_builds(mock_scrape_build):
    # Arrange
    mock_path_soup = Mock() # mock for the path soup
    mock_weapon_list = MagicMock() # mock for the weapon list
    mock_count = Mock() # mock for the placement in the weapon list
    # When weapon_list[count] is called return this instead:
    mock_weapon_list.__getitem__.return_value = "Mocked Weapon name"
    # when path_soup.find_all is called to get a list of builds use this instead
    # simulate a weapon having 4 builds
    mock_path_soup.find_all.return_value = [Mock(), Mock(), Mock(), Mock()]
    # each build when scraped will return this
    mock_scrape_build.return_value = (['ability1','ability2','ability3','ability4','ability5','ability6','ability7','ability8','ability9','ability10','ability11','ability12'], ['mode1','mode2'])
    # Action
    actual_output = scrape_all_builds(mock_path_soup, mock_weapon_list, mock_count) # the object the function returns
    # Assert  
    # Check if the returned object is a DataFrame
    assert isinstance(actual_output, pd.DataFrame)
    # Check if the dataframe has the right amount of entries
    assert len(actual_output) == 4
 # ----------------------------------------------------------

# END TESTING scrape_all_builds()

# START TESTING create_weapon_build_df()
# @patch('etl.extract.extract.make_request')
# @patch('bs4.BeautifulSoup')
# def test_create_weapon_build_df(mock_request, mock_soup_call):
#     # Arrange
#     path_list = [Mock(), Mock()]
#     weapon_list = [Mock(), Mock()]
#     mock_soup_call.return_value = Mock()
#     mock_request.return_value = Mock()
    
#     # Action
#     create_weapon_build_df(path_list, weapon_list)
    
    

# END TESTING create_weapon_build_df()
    


