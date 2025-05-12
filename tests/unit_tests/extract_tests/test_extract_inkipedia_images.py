from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


import pytest
from unittest.mock import patch, Mock
from requests.exceptions import Timeout, RequestException

from etl.extract.extract_inkipedia_images import extract_main_weapon_images
from etl.extract.extract_inkipedia_images import find_all_weapon_pages
from etl.extract.extract_inkipedia_images import find_weapon_path
from etl.extract.extract_inkipedia_images import fix_names
from etl.extract.extract_inkipedia_images import find_all_weapon_urls
from etl.extract.extract_inkipedia_images import find_all_images
from etl.extract.extract_inkipedia_images import find_image
from etl.extract.extract_inkipedia_images import start_session


# START TESTING extract_main_weapon_images()

# test if this returns a list
# replace the return values of these functions
@patch('etl.extract.extract_inkipedia_images.start_session')
@patch('etl.extract.extract_inkipedia_images.find_all_weapon_pages')
@patch('etl.extract.extract_inkipedia_images.find_all_weapon_urls')
def test_extract_main_weapon_images(mock_image_list, mock_path_list, mock_session):
    # Arrange
    w_names = ['weapon_1','weapon_2'] # example of a weapon names list
    mock_session.return_value = Mock() # mock the session
    mock_path_list.return_value = ['Path1', 'Path2'] # have the function return this
    mock_image_list.return_value = ['w_path1', 'w_path2'] # have the function return this
    expected_output = ['w_path1', 'w_path2'] # what we expect to see
    # Action
    actual_output = extract_main_weapon_images(w_names) # what is actually returned
    # Assert
    assert expected_output == actual_output # compare
    
# testing to see for when the weapon name list and image url list are equal

@patch('etl.extract.extract_inkipedia_images.start_session')
@patch('etl.extract.extract_inkipedia_images.find_all_weapon_pages')
@patch('etl.extract.extract_inkipedia_images.find_all_weapon_urls')
def test_extract_main_weapon_images_if_length_equal(mock_image_list, mock_path_list, mock_session):
    # Arrange
    w_names = ['weapon_1','weapon_2','weapon_3'] # weapon list of length 3
    mock_session.return_value = Mock() # mock the session
    mock_path_list.return_value = ['path1','path2','path3'] # path list of length 3
    mock_image_list.return_value = ['image1','image2','image3'] # images list of length 3
    expected_length = len(w_names) # what the length should be
    # Action
    actual_output = extract_main_weapon_images(w_names) # what list is returned
    # Assert
    assert len(actual_output) == expected_length # are the lengths equal?
    
    
# testing to see for when the weapon name list and image url list are NOT equal
# if there is an error
@patch('etl.extract.extract_inkipedia_images.start_session')
@patch('etl.extract.extract_inkipedia_images.find_all_weapon_pages')
@patch('etl.extract.extract_inkipedia_images.find_all_weapon_urls')
def test_extract_main_weapon_images_if_length_equal(mock_image_list, mock_path_list, mock_session):
    # Arrange
    w_names = ['weapon_1','weapon_2','weapon_3'] # weapon list of length 3
    mock_session.return_value = Mock()
    mock_path_list.return_value = ['path1','path2'] # path list of length 2
    mock_image_list.return_value = ['image1','image2']  # images list of length 2
    expected_length = len(w_names) # what the length should be
    
    # Assert
    # --- Assistance from ChatGPT -----------------
    # we should ge this error
    with pytest.raises(Exception):
        extract_main_weapon_images(w_names)
        
    # ----------------------------------------------

# FINISH TESTING extract_main_weapon_images()

# START TESTING find_all_weapon_pages()



# FINISH TESTING find_all_weapon_pages()


# START TESTING find_weapon_path()

 # Parameters we will use to test multiple example scenarios

# test to see if it returns a list (if name is in w_names)
@patch('etl.extract.extract_inkipedia_images.fix_names')
def test_find_weapon_path_allow(mock_fix_names):
    BASE_PATH = 'https://splatoonwiki.org'
    # an example of html for the link to a weapon page
    w = '<td><a href="/wiki/Sploosh-o-matic" title="Sploosh-o-matic"></a></td>'
    w = BeautifulSoup(w, 'html.parser').td  # convert to a html tag object
    path_list = [] # empty list to start with
    w_names = pd.Series(['Sploosh-o-matic']) # we know that this weapon is in the list
    mock_fix_names.return_value = 'Sploosh-o-matic' # so we are only testing one function simulate the response  of the other used
    expected_output = [BASE_PATH + w.find('a')['href']] # we expect the url to be added to the list
    
    actual_output = find_weapon_path(w, path_list, w_names) # what the list actually looks like
    
    assert expected_output == actual_output # comapare
    
# test to see if it returns a list (if name is NOT in w_names)
@patch('etl.extract.extract_inkipedia_images.fix_names')
def test_find_weapon_path_reject(mock_fix_names):
    BASE_PATH = 'https://splatoonwiki.org'
    # an example of wrong html for the link to a weapon page
    w = '<td><a href="/wiki/not_a_real_weapon" title="not a real weapon"></a></td>'
    w = BeautifulSoup(w, 'html.parser').td  # convert to a html tag object
    path_list = [] # empty list to start with
    w_names = pd.Series(['Sploosh-o-matic']) # we know that this weapon is in the list
    mock_fix_names.return_value = 'not a real weapon' # so we are only testing one function simulate the response  of the other used
    expected_output = [] # we expect the url to NOT be added to the list
    
    actual_output = find_weapon_path(w, path_list, w_names) # what the list actually looks like
    
    assert expected_output == actual_output # comapare
# FINISH TESTING find_weapon_path()


# START TESTING fix_names()

# observing the results of different cases
@pytest.mark.parametrize("name, expected_new_name", [
    ('Sploosh-o-matic', 'Sploosh-o-matic'),                     # nothing to change case
    ('Custom_Splattershot_Jr.', 'Custom Splattershot Jr.'),     # underscores to spaces case
    ('N-ZAP_%2785', "N-ZAP '85"),                               # weird cases with commas
    ('N-ZAP_%2789', "N-ZAP '89"),
    ('S-BLAST_%2792', "S-BLAST '92"),
    ('S-BLAST_%2791', "S-BLAST '91"),
    ('Z%2BF_Splat_Charger', "Z+F Splat Charger"),               # weird cases with + symbol
    ('Z%2BF_Splatterscope', "Z+F Splatterscope"),

])
# testing different names in urls to see if they are properly handled
def test_fix_names(name, expected_new_name):
    # Arrange
    expected_output = (expected_new_name) # what each name should look like after transformation
    # Action
    actual_output = fix_names(name) # what they actually look like
    # Assert
    assert expected_output == actual_output # comapare all these
    
# FINISHED TESTING fix_names()


# START TESTING find_all_images()

# testing to see if an image url is correctly added to the list if it IS NOT None
@patch('etl.extract.extract_inkipedia_images.find_image')
def test_find_all_images(mock_find_image):
    # Arrange
    soup = Mock() # mock this
    image_path_list = [] # start with empty list
    soup.find_all.return_value = ['image1','image2'] # mock soup object returns the found images
    mock_find_image.return_value = 'image url' # assume these meet the requirments and so return an image
    expected_output = ['image url'] #  this is added to this list, so we should have this
    # Action
    actual_output = find_all_images(soup,  image_path_list)  # the list we actually get
    # Assert
    assert actual_output == expected_output # compare
    
# testing to see if an image url is correctly added to the list if it IS None
@patch('etl.extract.extract_inkipedia_images.find_image')
def test_find_all_images_none(mock_find_image):
    # Arrange
    soup = Mock() # mock this
    image_path_list = [] # start with empty list
    soup.find_all.return_value = ['image1','image2'] # mock soup object returns the found images
    mock_find_image.return_value = None # assume these didn't meet the requirments and so return nothing
    expected_output = [] # the list should be unchanged
    # Action
    actual_output = find_all_images(soup,  image_path_list)  # the list we actually get
    # Assert
    assert actual_output == expected_output # compare
    
# FINISHED TESTING find_all_images()

# START TESTING find_image()

# test if the correct image found returns the url
def test_find_image_invalid():
    img = Mock() # don't need to have the actual image
    # return an example of an acceptable image's src 
    ex_src = '//cdn.wikimg.net/en/splatoonwiki/images/thumb/e/ed/S3_Weapon_Main_.52_Gal.png/256px-S3_Weapon_Main_.52_Gal.png'
    img.get.return_value = ex_src
    expected_output = 'https:' + ex_src # we expect to get the full url
    # Action
    actual_output = find_image(img)
    # Assert
    assert actual_output == expected_output
    

# test if the incorrect image found returns a None
def test_find_image_valid():
    img = Mock() # don't need to have the actual image
    # return an example of an unacceptable image's src 
    ex_src = '//cdn.wikimg.net/en/splatoonwiki/images/7/7f/Site-wordmark.svg'
    img.get.return_value = ex_src
    expected_output = None # we expect to get the full url
    # Action
    actual_output = find_image(img)
    # Assert
    assert actual_output == expected_output

# FINISHED TESTING find_image()

# START TESTING start_session()

# test if returns a session
def test_start_session():
    actual_output = start_session() # see what it returns
    assert isinstance(actual_output, requests.sessions.Session) # check if its this object type

# FINISHED TESTING start_session()





