from bs4 import BeautifulSoup
import requests
import pandas as pd

from etl.extract.extract import make_request


# defining constants:
SENDOU_BUILDS_URL = 'https://sendou.ink/builds'
SENDOU_BASE_URL = 'https://sendou.ink'




# function that returns the data extracted from sendou as a data frame

def extract_sendou_data():
    # call function that returns a list of paths to each weapon's page of builds and a list of weapon names
    # call function returns the dataframe
    return None


# function to find paths for weapon build pages
def weapon_build_paths():
    # making a request to 'https://sendou.ink/builds'
    soup = make_request(SENDOU_BUILDS_URL)
    
    paths = [] # empty list for storing paths
    weapon_names = [] # empty list for storing weapon names
    
    all_links = soup.find_all('a') # list of all hyperlinks on the page

    # loop through all the links
    for link in all_links: 
        href = link.get('href') # the href of attribute of <a>
        # make sure that the <a> has href
        if href is not None: 
            # if href is not none then continue to check if the link is for a weapon build page
            if href.startswith('/builds/'):
                # if it is add the link to the list (add to the end of the base path first)
                path = SENDOU_BASE_URL + href
                paths.append(path)
                # also find the text of the link (with strip remove whitespaces)
                # add this to the list of weapon names
                weapon_names.append(link.get_text(strip=True))
                
    #print(len(paths))
    #print(len(weapon_names))
    return paths, weapon_names




# function to create a dataframe from the the weapon build data
def create_weapon_build_df():
    return None


