import requests
from bs4 import BeautifulSoup as bs


word = input('Enter Word: ')
URL = 'https://www.lexico.com/en/definition/'+word

req = requests.get(URL)

soup = bs(req.content, 'html5lib')

all_def = soup.findAll('section', {'class': 'gramb'})


types = soup.findAll('span', {'class': 'pos'})

types_list = []

for Type in types:
    types_list.append(Type.text)

print(types_list)
