import json

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
params={}

# read API keys
with open('config_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)

myfile=open("latdatatwo.txt","a")
    
with open('fasfoodtwo.txt',"r") as f:

    for line in f: 
        params["term"] = line
        params["limit"]="1"
        params["actionlinks"]='true'
        response = client.search('San Francisco', **params)
        
        
        bizlist=response.businesses
        for biz in bizlist:
            
            print("\n["+str(biz.location.coordinate.latitude)+','+str(biz.location.coordinate.longitude)+'],')