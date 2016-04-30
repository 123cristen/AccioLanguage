# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.
import urllib2
import urllib
import sys
import base64
import json

def run():
	# Azure portal URL.
	base_url = 'https://westus.api.cognitive.microsoft.com/'
	# Your account key goes here.
	account_key = '934a947dbce44afd958025237aca7de0'

	headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
	            
	input_texts = '{"documents":[{"id":"1","text":"hola como estas?"},{"id":"2","text":"was ist das genau?"},{"id":"three","text":"hello my world"},]}'

	num_detect_langs = 1;

	# Detect key phrases.
	batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
	req = urllib2.Request(batch_keyphrase_url, input_texts, headers) 
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)
	for keyphrase_analysis in obj['documents']:
	    print('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases'])))

	# Detect language.
	language_detection_url = base_url + 'text/analytics/v2.0/languages' + ('?numberOfLanguagesToDetect=' + num_detect_langs if num_detect_langs > 1 else '')
	req = urllib2.Request(language_detection_url, input_texts, headers)
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)
	for language in obj['documents']:
	    print('Languages: ' + str(language['id']) + ': ' + ','.join([lang['name'] for lang in language['detectedLanguages']]))

	# Detect sentiment.
	batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
	req = urllib2.Request(batch_sentiment_url, input_texts, headers) 
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)
	for sentiment_analysis in obj['documents']:
	    print('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score']))
	    