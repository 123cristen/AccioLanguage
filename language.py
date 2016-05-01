# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.
import urllib2
import urllib
import sys
import base64
import json

def get_language(input_texts):
	# input_texts = "hi sunnie"
	# Azure portal URL.
	base_url = 'https://westus.api.cognitive.microsoft.com/'
	# Your account key goes here.
	account_key = '934a947dbce44afd958025237aca7de0'

	headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
	            
	input_texts = '{"documents":[{"id":"1","text":"' + input_texts + '"}]}'

	num_detect_langs = 1;



	# Detect languages
	language_detection_url = base_url + 'text/analytics/v2.0/languages' + ('?numberOfLanguagesToDetect=' + num_detect_langs if num_detect_langs > 1 else '')
	req = urllib2.Request(language_detection_url, input_texts, headers)
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)
	resultStr = ''
	for language in obj['documents']:
	    resultStr += 'Languages: '  + ': ' + ','.join([lang['name'] for lang in language['detectedLanguages']])
	return resultStr