# sentiments.py
import urllib2
import json

# Detect sentiment of input text
def get_sentiment(input_texts):
	# Azure portal URL and account key
	base_url = 'https://westus.api.cognitive.microsoft.com/'
	account_key = '934a947dbce44afd958025237aca7de0'
	headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
	
	# Format into JSON 
	input_texts = '{"documents":[{"id":"1","text":"' + input_texts +'"},]}'

	# Set request URL, send and read response
	batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
	req = urllib2.Request(batch_sentiment_url, input_texts, headers) 
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)

	# Save score to output
	score = ""
	for sentiment_analysis in obj['documents']:
	    score += str(sentiment_analysis['score'])
	return score
    