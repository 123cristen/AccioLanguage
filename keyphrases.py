# keyphrases.py
import urllib2
import json

# Extract key phrases from input text
def get_keyPhrases(input_texts):
	# Azure portal URL and account key
	base_url = 'https://westus.api.cognitive.microsoft.com/'
	account_key = '934a947dbce44afd958025237aca7de0'
	headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}

	# Format into JSON 
	input_texts = '{"documents":[{"id":"1","text":"' + input_texts + '"}]}'
	num_detect_langs = 1;

	# Set request URL, send and read response
	batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
	req = urllib2.Request(batch_keyphrase_url, input_texts, headers) 
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)

	# Save result for output
	resultStr = ''
	for keyphrase_analysis in obj['documents']:
	    resultStr+= ('Key phrases' + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases']))+ '\n')
	return resultStr