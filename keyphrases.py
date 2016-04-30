# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.
import urllib2
import urllib
import sys
import base64
import json

def get_keyPhrases(input_texts):
	# input_texts = "hi sunnie"
	# Azure portal URL.
	base_url = 'https://westus.api.cognitive.microsoft.com/'
	# Your account key goes here.
	account_key = '934a947dbce44afd958025237aca7de0'

	headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
	            
	input_texts = '{"documents":[{"id":"1","text":"' + input_texts + '"}]}'

	num_detect_langs = 1;
	# Detect key phrases.
	batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
	req = urllib2.Request(batch_keyphrase_url, input_texts, headers) 
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)
	resultStr = ''
	for keyphrase_analysis in obj['documents']:
	    resultStr+= ('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases']))+ '\n')
	# return input_texts
	return resultStr