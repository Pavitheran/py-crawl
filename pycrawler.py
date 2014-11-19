__author__ = 'Pavitheran'

import urllib.request
from bs4 import BeautifulSoup

def get_html_content(a_url):
##Consumes url string. Returns the raw HTML of given web page
    with urllib.request.urlopen(a_url) as file:
        raw_html = file.read()

    return raw_html


def all_urls(raw_html):
    ##Consumes raw HTML. Returns a list of all hyperlinks on page.
    soup = BeautifulSoup(raw_html)
    url_list = []
    for url in soup.find_all('a'):
        url_list.append(url.get('href'))
    return url_list

##make_soup(get_html_content("http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html"))