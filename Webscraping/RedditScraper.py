"""
This script is intended to list the top trending topics on the subreddit of your choice.
"""


from urllib.request import urlopen

import bs4
import urllib
from bs4 import BeautifulSoup as soup

# opening up connection, grabbing the page
def fetch_data(url):
    try:
        uClient = urlopen(url)
        page_html = uClient.read()
        uClient.close()

        # html parsing
        page_soup = soup(page_html, "html.parser")
        name_container = page_soup.findAll("a", {"data-click-id": "body"})

        for name in name_container:
            print(name.div.h3.text)
    except:
        print('...')
        return fetch_data(url)


subreddit = input('Enter the subreddit name: ')
fetch_data('https://www.reddit.com/r/' + subreddit)
input("Press enter to exit.")