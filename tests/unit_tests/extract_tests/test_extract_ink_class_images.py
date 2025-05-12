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
from etl.extract.extract_ink_class_images import extract_classes_images
from etl.extract.extract_ink_class_images import find_all_class_images
from etl.extract.extract_ink_class_images import find_class_image
from etl.extract.extract_ink_class_images import find_class_names
from etl.extract.extract_ink_class_images import create_class_df

# START TESTING extract_classs_images()

# test to see if the function returns a dataframe if the classs dataframe is 19 length long
@patch('etl.extract.extract_ink_class_images.create_class_df')
@patch('etl.extract.extract_ink_class_images.find_all_class_images')
@patch('etl.extract.extract_ink_class_images.find_class_names')
def test_extract_classes_images_11_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the weapons df
    mock_find_names.return_value = ['class1', 'class2'] # return list of classes
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['class_name'] * 11}) # return a dataframe object with 11 rows
    # Action
    actual_output = extract_classes_images(mock_df) # what is actually returned
    # Assert
    assert isinstance(actual_output, pd.DataFrame) # check to see if its a dataframe object
    
    
# test to see if the function returns a dataframe if the classs dataframe is NOT 19 length long
@patch('etl.extract.extract_ink_class_images.create_class_df')
@patch('etl.extract.extract_ink_class_images.find_all_class_images')
@patch('etl.extract.extract_ink_class_images.find_class_names')
def test_extract_classes_images_8_long(mock_find_names, mock_find_images, mock_create_df):
    # Arrange
    mock_df = Mock() # Mock the weapons df
    mock_find_names.return_value = ['class', 'class2'] # return list of classs
    mock_find_images.return_value = ['image1','image2'] # return list of images
    mock_create_df.return_value = pd.DataFrame({'testing': ['class_name'] * 8}) # return a dataframe object with 8 rows
    # Assert
    # when running the function we should get an exception error
    with pytest.raises(Exception):
        extract_classes_images(mock_df)

# FINISH TESTING extract_classs_images()


# START TESTING extract_classs_images()

# test to see if function accurately removes repeats and returns the correct dataframe
def test_find_class_names():
    # Arrange
    # test example of classes data in the weapons dataframe
    # includes repeats
    s_data = {
        'Class': ['class_a','class_a','class_b','class_c' ]
    }
    # use to create a dataframe to test with
    df_weapons = pd.DataFrame(s_data)
    # expected data
    exp_data = {
        'Weapon Class': ['class_a','class_b','class_c' ]
    }
    expected_df = pd.DataFrame(exp_data) # dataframe we expect to get
    # sort alphabetically and remove previous index for comparison
    expected_df = expected_df.sort_values('Weapon Class').reset_index(drop=True)
    # Action
    actual_df = find_class_names(df_weapons) # the actual data frame
    # sort alphabetically and remove previous index for comparison
    actual_df = actual_df.sort_values('Weapon Class').reset_index(drop=True)
    # Assert
    # compare to see if these dataframes match
    pd.testing.assert_frame_equal(expected_df, actual_df) 

# FINISH TESTING extract_classs_images()

# START TESTING find_class_image()

# observing the results of different images
@pytest.mark.parametrize("image, expected_list", [
    ('<img height="32" src="//cdn.wikimg.net/en/splatoonwiki/images/7/7f/Site-wordmark.svg" width="152"/>',
     []),   # not a class = empty list
    ('<img alt="" decoding="async" height="120" loading="lazy" src="//cdn.wikimg.net/en/splatoonwiki/images/thumb/0/0d/S3_Icon_Brella.png/120px-S3_Icon_Brella.png" srcset="//cdn.wikimg.net/en/splatoonwiki/images/0/0d/S3_Icon_Brella.png 1.5x" width="120"/>',
     ["https://cdn.wikimg.net/en/splatoonwiki/images/thumb/0/0d/S3_Icon_Brella.png/120px-S3_Icon_Brella.png"])
    
])

# testing if a class is either added to the list or not 
def test_find_class_image(image, expected_list):
    # Arrange
    input_image = image # the image
    input_image = BeautifulSoup(input_image, 'html.parser').img  # convert to a html img
    image_urls = [] # empty list to start with
    Expected_output = expected_list # what we expect the list to look like
    # Action
    Actual_output = find_class_image(input_image, image_urls) # what the list actually looks like
    # Assert
    assert Expected_output == Actual_output # compare

# START TESTING find_class_image()





# START TESTING create_class_df()

# testing to see if the correct dataframe is returned
def test_create_ability_df():
    # Arrange
    # data from prev test to show what the classs df could have in it
    s_data = {
        'Weapon Class': ['class_a','class_b','class_c' ]
    }
    # use to create dataframe to test with
    class_weapons_df = pd.DataFrame(s_data)
    # ex urls with the same class names at the end
    # but purposefully out of order to test the sorting
    image_urls = [
        'something_here/class_b',
        'something_here/class_c',
        'something_here/class_a',
        ]
    # the sorted data, combining both list and df
    exp_data = {
        'Weapon Class': ['class_a','class_b','class_c' ],
        'Image URL': ['something_here/class_a','something_here/class_b','something_here/class_c' ]
    } 
    Expected_df = pd.DataFrame(exp_data) # the expected df from this data
    
    # Action
    Actual_df = create_class_df(class_weapons_df, image_urls) # what dataframe is created
    
    # Assert
    pd.testing.assert_frame_equal(Expected_df, Actual_df) # check to see if they are the same
    

# END TESTING create_class_df()