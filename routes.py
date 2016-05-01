# routes.py
from sentiment import *
from keyphrases import *
from language import *

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template(
		'index.html',
		title = 'Accio',
	)

@app.route("/language")
def language():
	return render_template(
		'language.html',
		title = 'Language Detection',
	)

@app.route("/keyphrases")
def keyphrases():
  return render_template(
    'keyphrases.html',
    title = 'Key Phrase Detection',
  )

@app.route("/sentiment")
def sentiment():
	return render_template(
		'sentiment.html',
		title = 'Sentiment Detection',
	)

@app.route("/show_sentiment", methods=['POST'])
def show_sentiment():
	text = request.form['text_input']
	output = get_sentiment(text);
	return render_template(
		'show_sentiment.html',
		title = 'Sentiment Detection Results',
		score = output,
		text = text,
	)

@app.route('/keyAnswers', methods=['POST'])
def getKeyPhrases():
  text = request.form['text']
  output = get_keyPhrases(text)
  return render_template(
    'showKeyPhrases.html',
    title = 'Key Phrase Results',
    answers = output,
    text = text,
  )

@app.route('/languageAnswers', methods=['POST'])
def getLanguage():
  text = request.form['text']
  output = get_language(text)
  return render_template(
    'showLanguage.html',
    title = 'Language Detection Results',
    answers = output,
    text = text,
  )

if __name__ == "__main__":
    app.debug = True
    app.run()
