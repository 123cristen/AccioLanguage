# language.py
import urllib2
import json

# Detect languages of input text
def get_language(input_texts):
	# Azure portal URL and account key
	base_url = 'https://westus.api.cognitive.microsoft.com/'
	account_key = '934a947dbce44afd958025237aca7de0'
	headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
	
	# Format into JSON 
	input_texts = '{"documents":[{"id":"1","text":"' + input_texts + '"}]}'
	num_detect_langs = 1;

	# Set request URL, send and read response
	language_detection_url = base_url + 'text/analytics/v2.0/languages' + ('?numberOfLanguagesToDetect=' + num_detect_langs if num_detect_langs > 1 else '')
	req = urllib2.Request(language_detection_url, input_texts, headers)
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)

	# Save result for output
	resultStr = ''
	for language in obj['documents']:
	    resultStr += 'Languages'  + ': ' + ','.join([lang['name'] for lang in language['detectedLanguages']])
	return resultStr