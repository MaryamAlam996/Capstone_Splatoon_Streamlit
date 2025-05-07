from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def extract_data():
    return None

# function that takes in a site, makes a request then returns the response
def make_request(URL):
    try:
        # sending a get request to a URL, wait 10 seconds max for a response
        response = requests.get(URL, timeout=10) 
        if response.status_code != 200: # if the status code is not ok, return an error
            return {
                "status": "error",
                "error": "Request failed as status code is not 200"
            }
        # if succesful return response
        return response
    except Exception: 
        # return an error if something else goes wrong with the request
        return {
            "status": "error",
            "error": "An unknown error has occurred"
        }