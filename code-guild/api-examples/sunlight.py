__author__ = 'grant'

import requests
import pprint

userPhrase = input('What phrase are you looking for?')
query_params = { 'apikey': '0bfca639c9214f219d244705c7f1f90b',
				 'per_page': 3,
		   		 'phrase': userPhrase,
		   		 'sort': 'date desc'
		 		}

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get(endpoint, params=query_params)
data = response.json
#pprint.pprint(data)

legislator = data['results'][0]['speaker_first'] + ' ' + data['results'][0]['speaker_last']
date = data['results'][0]['date']
speech = data['results'][0]['speaking']
print("On " + date + ', ' + legislator + ' ' + "said:")
print("\'")
print(speech)