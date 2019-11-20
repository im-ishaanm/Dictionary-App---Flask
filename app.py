from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)


def searchWord(word):
    word = str(word)
    URL = 'https://www.lexico.com/en/definition/'+word

    req = requests.get(URL)

    soup = bs(req.content, 'html5lib')

    types = soup.findAll('span', {'class': 'pos'})

    types_list = []

    for Type in types:
        types_list.append(Type.text)

    ex_list = []
    examples = soup.findAll('div', {'class':'ex'})

    defs_list = []
    defs = soup.findAll('span', {'class':'ind'})

    for Def in defs:
        defs_list.append(Def.text)

    for Example in examples:
        ex_list.append(Example.text)
    
    # for Example in ex_list:
    #     if Example[0] == "'":
    #         Example[1].upper()
    #     else:
    #         Example[0].upper()

    return(types_list, defs_list, ex_list)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form['word']
        data = searchWord(word)
        return render_template('home.html', Word=word,  Type=data[0], Def=data[1], Ex=data[2])
    else:
        return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    app.run(debug=True)
