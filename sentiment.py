import urllib2
import urllib
import sys
import base64
import json
            
#input_texts = '{"documents":[{"id":"1","text":"hola como estas?"},{"id":"2","text":"was ist das genau?"},{"id":"three","text":"hello my world"},]}'

def create_json(text):
	return '{"documents":["text":"'+text+'"]}'


# Detect sentiment.
def find_sentiment(input_texts):
	# Azure portal URL.
	base_url = 'https://westus.api.cognitive.microsoft.com/'
	# Your account key goes here.
	account_key = '934a947dbce44afd958025237aca7de0'
	headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
	#input_texts = '{"documents":[{"id":"1","text":"hola como estas?"},{"id":"2","text":"was ist das genau?"},{"id":"three","text":"hello my world"},]}'

	batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
	req = urllib2.Request(batch_sentiment_url, input_texts, headers) 
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)
	output_texts = ""
	for sentiment_analysis in obj['documents']:
	    output_texts += 'Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score'])+ "\n"
	return output_texts
    