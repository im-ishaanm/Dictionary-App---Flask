from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)


def searchWord(word):
    word = str(word)
    URL = 'https://www.merriam-webster.com/dictionary/'+word
    req = requests.get(URL)
    soup = bs(req.content, 'html5lib')

    types = soup.findAll('a', {'class': 'important-blue-link'})
    defin = soup.findAll('span', {'class': 'dtText'})

    defin = defin[0].text
    defin = defin.replace(':', '', 1)

    return [word, types[0].text, defin]


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form['word']
        data = searchWord(word)
        return render_template('home.html', Word=data[0], Type=data[1], Defin=data[2])
    else:
        return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    app.run(debug=True)
