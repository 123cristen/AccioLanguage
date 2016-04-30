#flasky.py
import main
from keyphrases import *

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
  input_texts = '{"documents":[{"id":"1","text":"hola como estas?"},{"id":"2","text":"was ist das genau?"},{"id":"three","text":"hello my world"},]}'

  # result=keyPhrases_setup(input_texts)
  return render_template(
    'keyphrases.html',
    # body=result,
    title='AccioLanguage | Key Phrases',
  )

@app.route("/sentiment")
def sentiment():
  return render_template(
    'sentiment.html',
    title='AccioLanguage | Sentiment Detection',
  )


@app.route('/answers', methods=['POST'])
def key_report():
    text = request.form['text']
    text = text.upper()
    output = get_keyPhrases(text)
    # return output
    return render_template(
      'keyreport.html',
      title='AccioLanguage | Key Phrases | Report',
      answers= output,
    )

if __name__ == "__main__":
    app.debug=True
    app.run()
