import requests

URL = 'https://en.wikipedia.org/wiki/List_of_conflicts_in_Europe'
page = requests.get(URL)

print(page)
