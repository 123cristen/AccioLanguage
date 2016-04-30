#flasky.py
import main
import urllib
import urllib2
import json
from sentiment import *

from flask import render_template, request, Flask
app = Flask(__name__)

@app.route("/")
def home():
	return render_template(
		'index.html',
		title='AccioLanguage',
	)

@app.route("/language")
def language():
	return render_template(
		'language.html',
		title='AccioLanguage | Language Detection',
	)

@app.route("/keyphrases")
def keyphrases():
	return render_template(
		'keyphrases.html',
		title='AccioLanguage | Key Phrases',
	)

@app.route("/sentiment")
def sentiment():
	return render_template(
		'sentiment.html',
		title='AccioLanguage | Sentiment Detection',
		outputs = None,
	)

@app.route("/get_sentiment", methods=['POST'])
def get_sentiment():
	return request.form['text_input']



if __name__ == "__main__":
		app.debug = True
		app.run()