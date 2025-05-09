import pytest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
import requests
from unittest.mock import patch
from requests.exceptions import Timeout, RequestException

from etl.extract.url_request import make_request
from etl.extract.extract_sendou_builds import weapon_build_paths
from etl.extract.extract_sendou_builds import search_for_build_path


# testing successful request (test code from web scraping repo)
@patch('requests.get')   
def test_make_request_success(mock_get):
    mock_get.return_value.status_code = 200 # returns OK status code
    make_request('https://www.google.com/') # mock HTML
    mock_get.assert_called_once_with('https://www.google.com/', timeout=10)
        
# testing handling of unsuccessful request (test code from web scraping repo)
@patch('requests.get') 
def test_make_request_fail(mock_get):
    mock_get.return_value.status_code = 404
    result = make_request('https://www.google.com/')
    assert result == {
        "status": "error",
        "error": "Request failed as status code is not 200"
    }