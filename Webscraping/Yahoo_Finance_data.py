import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def fetch_price(url):
    try:
        uClient = urlopen(url)
        page_html = uClient.read()
        uClient.close()

        # html parsing
        page_soup = soup(page_html, "html.parser")
        name_container = page_soup.findAll("div", {"id": "quote-header-info"})
        price_container = page_soup.findAll("div", {"data-reactid": "12"})

        name = name_container[0]
        print(name.h1.text)

        price = price_container[0]
        print("Price: " + price.div.span.text + " , " + price.div.div.span.text)


    except:
        print('Unable to find data.')

def fetch_info(url):
    try:
        uClient = urlopen(url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        peg_container = page_soup.findAll("td", {"data-reactid": "138"})

        info = peg_container[0]
        print("PEG Ratio (5 yr expected): " + info.text)
    except:
        print('Unable to fetch PEG data')



symbol = input('Enter the symbol of the company: ').strip()
fetch_price('https://finance.yahoo.com/quote/' + symbol)
fetch_info('https://finance.yahoo.com/quote/' + symbol + '/key-statistics?p=' + symbol)
input('Press enter to exit program.')




