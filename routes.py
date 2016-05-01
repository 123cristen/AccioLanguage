#flasky.py
import main
from keyphrases import *
from language import *
from flask import render_template, Flask, request
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
    title='AccioLanguage | Key Phrases Detection',
  )

@app.route("/sentiment")
def sentiment():
  return render_template(
    'sentiment.html',
    title='AccioLanguage | Sentiment Detection',
  )


@app.route('/keyAnswers', methods=['POST'])
def getKeyPhrases():
    text = request.form['text']
    output = get_keyPhrases(text)
    return render_template(
      'showKeyPhrases.html',
      title='AccioLanguage | Key Phrases Detection',
      answers= output,
    )
@app.route('/languageAnswers', methods=['POST'])
def getLanguage():
    text = request.form['text']
    output = get_language(text)
    return render_template(
      'showLanguage.html',
      title='AccioLanguage | Language Detection',
      answers= output,
    )

if __name__ == "__main__":
    app.debug=True
    app.run()
