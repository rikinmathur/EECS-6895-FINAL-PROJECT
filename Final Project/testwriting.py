import json

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# read API keys
with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

#terms= ['KFC']
#for term in terms:
params = {
	'terms': 'parks, all',
  'lang': 'en',
  'sort': '1',    		
  'radius_filter':'40000',	
}
response = client.search('San Francisco', **params)

bizlist=response.businesses
for biz in bizlist:
    print biz.url

