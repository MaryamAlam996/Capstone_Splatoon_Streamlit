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
from etl.extract.extract_ink_sub_images import extract_subs_images
from etl.extract.extract_ink_sub_images import find_all_sub_images
from etl.extract.extract_ink_sub_images import find_sub_image
from etl.extract.extract_ink_sub_images import find_sub_names
from etl.extract.extract_ink_sub_images import create_sub_df

# START TESTING extract_subs_images()

# test to see if the function returns a dataframe if the subs dataframe is 19 length long
@patch('etl.extract.extract_ink_sub_images.create_sub_df')
@patch('etl.extract.extract_ink_sub_images.find_all_sub_images')
@patch('etl.extract.extract_ink_sub_images.find_sub_names')
def test_extract_subs_images_14_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the weapons df
    mock_find_names.return_value = ['specia1', 'sub2'] # return list of subs
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['sub_name'] * 14}) # return a dataframe object with 14 rows
    # Action
    actual_output = extract_subs_images(mock_df) # what is actually returned
    # Assert
    assert isinstance(actual_output, pd.DataFrame) # check to see if its a dataframe object
    
    
# test to see if the function returns a dataframe if the subs dataframe is NOT 19 length long
@patch('etl.extract.extract_ink_sub_images.create_sub_df')
@patch('etl.extract.extract_ink_sub_images.find_all_sub_images')
@patch('etl.extract.extract_ink_sub_images.find_sub_names')
def test_extract_subs_images_12_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the weapons df
    mock_find_names.return_value = ['specia1', 'sub2'] # return list of subs
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['sub_name'] * 12}) # return a dataframe object with 12 rows
    # Assert
    # when running the function we should get an exception error
    with pytest.raises(Exception):
        extract_subs_images(mock_df)

# FINISH TESTING extract_subs_images()


# START TESTING extract_subs_images()

# test to see if function accurately removes repeats and returns the correct dataframe
def test_find_sub_names():
    # Arrange
    # test example of subs data in the weapons dataframe
    # includes repeats
    s_data = {
        'Sub': ['sub_a','sub_a','sub_b','sub_c' ]
    }
    # use to create a dataframe to test with
    df_weapons = pd.DataFrame(s_data)
    # expected data
    exp_data = {
        'Sub Weapon': ['sub_a','sub_b','sub_c' ]
    }
    expected_df = pd.DataFrame(exp_data) # dataframe we expect to get
    # sort alphabetically and remove previous index for comparison
    expected_df = expected_df.sort_values('Sub Weapon').reset_index(drop=True)
    # Action
    actual_df = find_sub_names(df_weapons) # the actual data frame
    # sort alphabetically and remove previous index for comparison
    actual_df = actual_df.sort_values('Sub Weapon').reset_index(drop=True)
    # Assert
    # compare to see if these dataframes match
    pd.testing.assert_frame_equal(expected_df, actual_df) 

# FINISH TESTING extract_subs_images()

# START TESTING find_sub_image()

# observing the results of different images
@pytest.mark.parametrize("image, expected_list", [
    ('<img height="32" src="//cdn.wikimg.net/en/splatoonwiki/images/7/7f/Site-wordmark.svg" width="152"/>',
     []),   # not a sub = empty list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/3/3a/S3_Weapon_Sub_Angle_Shooter_Flat.png" width="120"/>',
     ["https://cdn.wikimg.net/en/splatoonwiki/images/3/3a/S3_Weapon_Sub_Angle_Shooter_Flat.png"]),   # a flat image of a sub = add to the list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/d/d4/S3_Weapon_Sub_Angle_Shooter.png/120px-S3_Weapon_Sub_Angle_Shooter.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/d/d4/S3_Weapon_Sub_Angle_Shooter.png 1.5x" width="120"/>',
     []),   # non flat image of a sub = empty list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/1/12/S3_Weapon_Sub_Smallfry.png" width="120"/>',
     [])    # small fry = empty list
])

# testing if a sub is either added to the list or not 
def test_find_sub_image(image, expected_list):
    # Arrange
    input_image = image # the image
    input_image = BeautifulSoup(input_image, 'html.parser').img  # convert to a html img
    image_urls = [] # empty list to start with
    Expected_output = expected_list # what we expect the list to look like
    # Action
    Actual_output = find_sub_image(input_image, image_urls) # what the list actually looks like
    # Assert
    assert Expected_output == Actual_output # compare

# START TESTING find_sub_image()





# START TESTING create_sub_df()

# testing to see if the correct dataframe is returned
def test_create_ability_df():
    # Arrange
    # data from prev test to show what the subs df could have in it
    s_data = {
        'Sub Weapon': ['sub_a','sub_b','sub_c' ]
    }
    # use to create dataframe to test with
    sub_weapons_df = pd.DataFrame(s_data)
    # ex urls with the same sub names at the end
    # but purposefully out of order to test the sorting
    image_urls = [
        'something_here/sub_b',
        'something_here/sub_c',
        'something_here/sub_a',
        ]
    # the sorted data, combining both list and df
    exp_data = {
        'Sub Weapon': ['sub_a','sub_b','sub_c' ],
        'Image URL': ['something_here/sub_a','something_here/sub_b','something_here/sub_c' ]
    } 
    Expected_df = pd.DataFrame(exp_data) # the expected df from this data
    
    # Action
    Actual_df = create_sub_df(sub_weapons_df, image_urls) # what dataframe is created
    
    # Assert
    pd.testing.assert_frame_equal(Expected_df, Actual_df) # check to see if they are the same
    

# END TESTING create_sub_df()