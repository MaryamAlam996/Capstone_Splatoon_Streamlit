import pytest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
import requests
from unittest.mock import patch
from requests.exceptions import Timeout, RequestException
from bs4 import BeautifulSoup

from etl.extract.extract_sendou_builds import make_request
from etl.extract.extract_sendou_builds import weapon_build_paths
from etl.extract.extract_sendou_builds import search_for_build_path



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