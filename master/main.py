import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/HTML'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
