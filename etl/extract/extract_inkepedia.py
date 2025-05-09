
from bs4 import BeautifulSoup
# import requests
import time
import pandas as pd
from etl.extract.url_request import make_request

# defining constants

ALL_WEAPONS_SITE = (
    'https://splatoonwiki.org/wiki/List_of_main_weapons_in_Splatoon_3'
)


# function to extract all the needed data from inkepedia
def extract_inkepedia():
    weapon_details_df = extract_weapon_details()
    return weapon_details_df


# function to specifically extract the information for each main weapon
# returns a dataframe
def extract_weapon_details():
    # make a request to the website
    soup = BeautifulSoup(make_request(ALL_WEAPONS_SITE).text, "html.parser")
    # call function to return all the weapon details from the site
    weapon_info_list = scrape_weapon_details(soup)
    # call function to reshape this list to be a 2d array
    complete_list = reshaping_weapon_details(weapon_info_list)
    # use each element from this 2d array as a row in a dataframe
    # this way each weapon has a row describing it
    weapons_df = pd.DataFrame(complete_list, columns=[
        'Extra_space', 'Name', 'ID', 'Sub', 'Special',
        'Special_Points', 'Level', 'Price', 'Class', 'Introduced'
    ])
    # some of these columns are unnessary and we will drop them later
    # return the created dataframe
    return weapons_df


# function to find weapon details as a 1d array
def scrape_weapon_details(soup):
    # find all the rows in the weapons table
    all_rows = soup.find_all('tr')
    weapon_info_list = []  # empty list to store these
    # loop through eah row
    for row in all_rows:
        # function that adds elements from the row to the list
        weapon_info_list = scrape_row(row, weapon_info_list)
    # return this list
    return weapon_info_list


# function to find and return elements from row
# and append to a list of elements
def scrape_row(row, element_list):
    # short pause to not overwhelm the site
    time.sleep(0.05)
    # find all the elements in the row
    element = row.find_all('td')
    # loop through each
    for i in element:
        # add the text of the element to the list
        element_list.append(i.get_text(strip=True))
    return element_list


# function that takes the weapon details list
# and creates a 2d array with from it
def reshaping_weapon_details(weapon_info_list):
    complete_list = []  # 2d array to store detail lists for each weapon
    # looping through the list but in steps of 10
    for elm in range(0, len(weapon_info_list), 10):
        # create a list for each weapon
        # includes elements like name to the version it was introduced
        one_weapon = weapon_info_list[elm:elm+10]
        # add to the 2d array
        complete_list.append(one_weapon)
    # return the completed list of weapons lists
    return complete_list
