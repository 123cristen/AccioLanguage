#flasky.py
import main

from flask import render_template, Flask
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
  )

if __name__ == "__main__":
    app.run()