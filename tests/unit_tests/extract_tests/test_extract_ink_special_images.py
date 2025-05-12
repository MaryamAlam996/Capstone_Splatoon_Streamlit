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
from etl.extract.extract_ink_special_images import extract_specials_images
from etl.extract.extract_ink_special_images import find_all_special_images
from etl.extract.extract_ink_special_images import find_special_image
from etl.extract.extract_ink_special_images import find_special_names
from etl.extract.extract_ink_special_images import create_special_df

# START TESTING extract_specials_images()

# test to see if the function returns a dataframe if the specials dataframe is 19 length long
@patch('etl.extract.extract_ink_special_images.create_special_df')
@patch('etl.extract.extract_ink_special_images.find_all_special_images')
@patch('etl.extract.extract_ink_special_images.find_special_names')
def test_extract_specials_images_19_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the weapons df
    mock_find_names.return_value = ['specia1', 'special2'] # return list of specials
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['special_name'] * 19}) # return a dataframe object with 19 rows
    # Action
    actual_output = extract_specials_images(mock_df) # what is actually returned
    # Assert
    assert isinstance(actual_output, pd.DataFrame) # check to see if its a dataframe object
    
    
# test to see if the function returns a dataframe if the specials dataframe is NOT 19 length long
@patch('etl.extract.extract_ink_special_images.create_special_df')
@patch('etl.extract.extract_ink_special_images.find_all_special_images')
@patch('etl.extract.extract_ink_special_images.find_special_names')
def test_extract_specials_images_16_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the weapons df
    mock_find_names.return_value = ['specia1', 'special2'] # return list of specials
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['special_name'] * 16}) # return a dataframe object with 16 rows
    # Assert
    # when running the function we should get an exception error
    with pytest.raises(Exception):
        extract_specials_images(mock_df)

# FINISH TESTING extract_specials_images()


# START TESTING extract_specials_images()

# test to see if function accurately removes repeats and returns the correct dataframe
def test_find_special_names():
    # Arrange
    # test example of specials data in the weapons dataframe
    # includes repeats
    s_data = {
        'Special': ['Special_a','Special_a','Special_b','Special_c' ]
    }
    # use to create a dataframe to test with
    df_weapons = pd.DataFrame(s_data)
    # expected data
    exp_data = {
        'Special': ['Special_a','Special_b','Special_c' ]
    }
    expected_df = pd.DataFrame(exp_data) # dataframe we expect to get
    # sort alphabetically and remove previous index for comparison
    expected_df = expected_df.sort_values('Special').reset_index(drop=True)
    # Action
    actual_df = find_special_names(df_weapons) # the actual data frame
    # sort alphabetically and remove previous index for comparison
    actual_df = actual_df.sort_values('Special').reset_index(drop=True)
    # Assert
    # compare to see if these dataframes match
    pd.testing.assert_frame_equal(expected_df, actual_df) 

# FINISH TESTING extract_specials_images()

# START TESTING find_special_image()

# observing the results of different images
@pytest.mark.parametrize("image, expected_list", [
    ('<img height="32" src="//cdn.wikimg.net/en/splatoonwiki/images/7/7f/Site-wordmark.svg" width="152"/>',
     []),   # not a special = empty list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/e/ef/S3_Weapon_Special_Big_Bubbler.png/120px-S3_Weapon_Special_Big_Bubbler.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/e/ef/S3_Weapon_Special_Big_Bubbler.png 1.5x" width="120"/>',
     ["https://cdn.wikimg.net/en/splatoonwiki/images/thumb/e/ef/S3_Weapon_Special_Big_Bubbler.png/120px-S3_Weapon_Special_Big_Bubbler.png"]), # a special = add to list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/b/b8/S3_Weapon_Special_Rainmaker.png/120px-S3_Weapon_Special_Rainmaker.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/b/b8/S3_Weapon_Special_Rainmaker.png 1.5x" width="120"/>',
     []), # rainmaker = empty list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/2/23/S3_Weapon_Special_Splashdown.png/120px-S3_Weapon_Special_Splashdown.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/2/23/S3_Weapon_Special_Splashdown.png 1.5x" width="120"/>',
     []), # splashdown = empty list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/b/b3/S3_Weapon_Special_Triple_Splashdown.png/120px-S3_Weapon_Special_Triple_Splashdown.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/b/b3/S3_Weapon_Special_Triple_Splashdown.png 1.5x" width="120"/>',
     ["https://cdn.wikimg.net/en/splatoonwiki/images/thumb/b/b3/S3_Weapon_Special_Triple_Splashdown.png/120px-S3_Weapon_Special_Triple_Splashdown.png"]), # triple splashdown = add to list
])

# testing if a special is either added to the list or not 
def test_find_special_image(image, expected_list):
    # Arrange
    input_image = image # the image
    input_image = BeautifulSoup(input_image, 'html.parser').img  # convert to a html img
    image_urls = [] # empty list to start with
    Expected_output = expected_list # what we expect the list to look like
    # Action
    Actual_output = find_special_image(input_image, image_urls) # what the list actually looks like
    # Assert
    assert Expected_output == Actual_output # compare

# START TESTING find_special_image()





# START TESTING create_special_df()

# testing to see if the correct dataframe is returned
def test_create_ability_df():
    # Arrange
    # data from prev test to show what the specials df could have in it
    s_data = {
        'Special': ['Special_a','Special_b','Special_c' ]
    }
    # use to create dataframe to test with
    special_weapons_df = pd.DataFrame(s_data)
    # ex urls with the same special names at the end
    # but purposefully out of order to test the sorting
    image_urls = [
        'something_here/Special_b',
        'something_here/Special_c',
        'something_here/Special_a',
        ]
    # the sorted data, combining both list and df
    exp_data = {
        'Special': ['Special_a','Special_b','Special_c' ],
        'Image URL': ['something_here/Special_a','something_here/Special_b','something_here/Special_c' ]
    } 
    Expected_df = pd.DataFrame(exp_data) # the expected df from this data
    
    # Action
    Actual_df = create_special_df(special_weapons_df, image_urls) # what dataframe is created
    
    # Assert
    pd.testing.assert_frame_equal(Expected_df, Actual_df) # check to see if they are the same
    

# END TESTING create_special_df()