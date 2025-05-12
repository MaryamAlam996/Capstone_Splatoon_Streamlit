from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

import pytest
from unittest.mock import patch, Mock
from requests.exceptions import Timeout, RequestException

from etl.extract.extract_ink_ability_images import extract_ability_images
from etl.extract.extract_ink_ability_images import find_ability_names
from etl.extract.extract_ink_ability_images import find_all_ability_images
from etl.extract.extract_ink_ability_images import find_ability_image
from etl.extract.extract_ink_ability_images import create_ability_df

# START TESTING extract_ability_images()


# test to see if the function returns a dataframe if the abilities dataframe is 26 length long
@patch('etl.extract.extract_ink_ability_images.create_ability_df')
@patch('etl.extract.extract_ink_ability_images.find_all_ability_images')
@patch('etl.extract.extract_ink_ability_images.find_ability_names')
def test_extract_ability_images_26_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the builds df
    mock_find_names.return_value = ['ability1', 'ability2'] # return list of abilities
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['ability_name'] * 26}) # return a dataframe object with 26 rows
    actual_output = extract_ability_images(mock_df) # what is actually returned
    assert isinstance(actual_output, pd.DataFrame) # check to see if its a dataframe object
    

# test to see if the function raises and error if not 26 long list
@patch('etl.extract.extract_ink_ability_images.create_ability_df')
@patch('etl.extract.extract_ink_ability_images.find_all_ability_images')
@patch('etl.extract.extract_ink_ability_images.find_ability_names')
def test_extract_ability_images_24_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the builds df
    mock_find_names.return_value = ['ability1', 'ability2'] # return list of abilities
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['ability_name'] * 24}) # return a dataframe object with 24 rows
    # when running the function we should get an exception error
    with pytest.raises(Exception):
        extract_ability_images(mock_df)


# FINISH TESTING extract_ability_images()

# START TESTING find_ability_names(df_builds)

def test_find_ability_names():
    # Arrange
    # test example of abilities data in the builds dataframe
    # here there are items unique to that type of gear
    # as well some that repeat both across and within gear type
    ab_data = {
        'Main_1': ['ability_a', 'ability_a', 'ability_b', 'ability_c', 'head_ability'],
        'Main_2': ['ability_a', 'ability_b', 'ability_b', 'ability_c', 'cloth_ability'],
        'Main_3': ['ability_a', 'ability_b', 'ability_c', 'ability_c', 'shoe_ability']
    } 
    # use to create dataframe to test with
    df_builds = pd.DataFrame(ab_data)
    # data we expect to be in the transformed dataframe
    exp_data = {
        'Abilities': ['ability_a', 'ability_b', 'ability_c', 'head_ability','cloth_ability','shoe_ability']
    }
    expected_df = pd.DataFrame(exp_data) # dataframe we expect to get
    # sort alphabetically and remove previous index for comparison
    expected_df = expected_df.sort_values('Abilities').reset_index(drop=True)
    # Action
    actual_df = find_ability_names(df_builds)
    # sort alphabetically and remove previous index for comparison
    actual_df = actual_df.sort_values('Abilities').reset_index(drop=True)
    # Assert
    # --- Assistance from ChatGPT ---------------------------------------
    # compare to see if these dataframes match
    pd.testing.assert_frame_equal(expected_df, actual_df)
    # -------------------------------------------------------------------


# FINISHED TESTING find_ability_names(df_builds)


# START TESTING find_all_ability_images()

# @patch('etl.extract.extract_ink_ability_images.find_ability_image')
# @patch('etl.extract.extract_ink_ability_images.make_request')
# def test_find_all_ability_images(mock_request, mock_find_image):
#     mock_response = Mock()
#     mock_response.text = Mock()
#     mock_request.return_value = mock_response
#     mock_soup = mock_request.return_value
#     mock_soup.find_all.return_value = ['Image1', 'Image2']
#     mock_find_image.return_value = ['imageUrl1', 'ImageURL2']
#     # Action
#     actual_output = find_all_ability_images()
    


# FINISHED TESTING find_all_ability_images()

# START TESTING find_ability_image()


# observing the results of different images
@pytest.mark.parametrize("image, expected_list", [
    ('<img height="32" src="//cdn.wikimg.net/en/splatoonwiki/images/7/7f/Site-wordmark.svg" width="152"/>',
     []),   # not an ability = empty list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/0/09/S3_Ability_Comeback.png/120px-S3_Ability_Comeback.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/0/09/S3_Ability_Comeback.png 1.5x" width="120"/>',
     ["https://cdn.wikimg.net/en/splatoonwiki/images/thumb/0/09/S3_Ability_Comeback.png/120px-S3_Ability_Comeback.png"]), # an ability = add the url
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/8/80/S3_Ability_Locked.png/120px-S3_Ability_Locked.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/8/80/S3_Ability_Locked.png 1.5x" width="120"/>',
     []) # locked ability = empty list
])

# testing if an ability is either added to the list or not 
def test_find_ability_image(image, expected_list):
    # Arrange
    input_image = image # the image
    input_image = BeautifulSoup(input_image, 'html.parser').img  # convert to a html img
    image_urls = [] # empty list to start with
    Expected_output = expected_list # what we expect the list to look like
    # Action
    Actual_output = find_ability_image(input_image, image_urls) # what the list actually looks like
    # Assert
    assert Expected_output == Actual_output # compare

# FINISHED TESTING find_ability_image()


# START TESTING create_ability_df()


def test_create_ability_df():
    # Arrange
    # data from prev test to show what the abilities df could have in it
    ab_data = {
        'Abilities': ['ability_a', 'ability_b', 'ability_c', 'head_ability','cloth_ability','shoe_ability']
    }
    # use to create dataframe to test with
    abilities_df = pd.DataFrame(ab_data)
    # ex urls with the same ability names at the end
    # but purposefully out of order to test the sorting
    image_urls = [
        'something_here/shoe_ability', 'something_here/ability_b',
        'something_here/ability_a', 'something_here/ability_c',
        'something_here/head_ability','something_here/cloth_ability'
        ]
    # the sorted data, combining both list and df
    exp_data = {
        'Abilities': ['ability_a', 'ability_b', 'ability_c', 'cloth_ability', 'head_ability','shoe_ability'],
        'Image URL': ['something_here/ability_a', 'something_here/ability_b', 'something_here/ability_c', 'something_here/cloth_ability', 'something_here/head_ability','something_here/shoe_ability']
    } 
    Expected_df = pd.DataFrame(exp_data) # the expected df from this data
    
    # Action
    Actual_df = create_ability_df(abilities_df, image_urls) # what dataframe is created
    
    # Assert
    pd.testing.assert_frame_equal(Expected_df, Actual_df) # check to see if they are the same
    

# END TESTING create_ability_df()