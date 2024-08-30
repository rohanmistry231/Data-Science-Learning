# Scrapes all url links from a page

import requests
from bs4 import BeautifulSoup
import pprint
import re
import pandas as pd

def scraper():
    baseurl = input("Enter the url you want scrape.. ")
    page = requests.get(baseurl)
    soup = BeautifulSoup(page.text, 'html.parser')

    urlAddress = []
    urlName = []
    for link in soup.find_all('a', attrs={'href': re.compile("^http")}):
        # ^http means fetching only those link which starts with http
            pprint.pprint(f"{link.string} ---> {link.get('href')}")
            urlName.append(link.string)
            urlAddress.append(link.get('href'))
    df = pd.DataFrame(list(zip(urlName, urlAddress)), columns=['Name','Link'])
    df.to_csv("csv_file.csv")

scraper()
