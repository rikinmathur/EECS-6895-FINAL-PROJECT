import json

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
params={}

# read API keys
with open('config_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)
        
with open("latdatafour.txt","a") as myfile:
    myfile.write("\n"+"PlaceName"+","+'latitude'+","+'Longitude'+','+'Rating'+'\n')
    f=open('placesnames.txt')

nameread = [line.rstrip('\n') for line in f]
for names in nameread:
    params["term"] = names
    params["limit"]="1"
    params["actionlinks"]='true'
    response = client.search('San Francisco', **params)

    bizlist=response.businesses
    for biz in bizlist:
        print(biz.rating)           