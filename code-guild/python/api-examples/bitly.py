__author__ = 'grant'

import requests
import json

"""API_KEY is just a place holder"""

query_params = {'access_token': 'API_KEY',
        'query': 'pizza',
        'limit': 10}

endpoint = 'https://api-ssl.bitly.com/v3/search'
response = requests.get(endpoint, params=query_params)

data = json.loads(response.content)
print(data)
