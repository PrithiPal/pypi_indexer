import sys
import os 
import requests
from bs4 import BeautifulSoup
 

ALL_PYPI_URL_LINK = "https://pypi.org/simple/"
ALL_PYPI_URL_FILENAME = "pypi_simple.html"




def download_webpage() : 
    r = requests.get(ALL_PYPI_URL_LINK)
    html_file = open(ALL_PYPI_URL_FILENAME,"w")
    html_file.write(r.text)
    html_file.close()    

def parse_webpage() : 
    soup = BeautifulSoup(open(ALL_PYPI_URL_FILENAME), features="lxml")
    print(soup.prettify())


def main() : 

    download_webpage()
    parse_webpage()


if __name__=='__main__' : 
    main()
