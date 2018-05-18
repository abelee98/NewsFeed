from flask import Flask, render_template, request
import json
import requests
app = Flask(__name__)

"""
API Key: ebe770cef0d04a64b163281dfa2541c0
sources: https://newsapi.org/v2/sources?apiKey=ebe770cef0d04a64b163281dfa2541c0
""" 
url_source = 'https://newsapi.org/v2/sources?apiKey=ebe770cef0d04a64b163281dfa2541c0'
response_source = requests.get(url_source)
source_json = response_source.json()

@app.route('/')
def index():
    return render_template('index.html', sources=source_json)

@app.route('/news', methods=['POST'])
def news():
    n = request.form['news']
    names = n.split(',')
    source = 'sources={}&'.format(names[0])
    url = ('https://newsapi.org/v2/top-headlines?'+
          source+
          'apiKey=ebe770cef0d04a64b163281dfa2541c0')
    response = requests.get(url)
    return render_template('news.html', news=response.json(), provider=names[1])