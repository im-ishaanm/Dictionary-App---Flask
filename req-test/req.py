import requests
from bs4 import BeautifulSoup as bs


word = input('Enter Word: ')
URL = 'https://www.merriam-webster.com/dictionary/'+word

req = requests.get(URL)

soup = bs(req.content, 'html5lib')

types = soup.findAll('a', {'class': 'important-blue-link'})


defin = soup.findAll('span', {'class': 'sb-0'})

d1 = defin[0].findChildren('span', {'class': 'dtText'})

print(d1[0].text)

print('Types are : ')
for type in types:
    print(type.text)

print('Definitons: ')
for d in defin:
    print(d.text)
