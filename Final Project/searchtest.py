import json
import time

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

def main():
	locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
	api_calls = []
	for lat,long in locations:
		params = get_search_parameters(lat,long)
		api_calls.append(get_results(params))
		#Be a good internet citizen and rate-limit yourself
		time.sleep(1.0)
		
	##Do other processing	

def get_results(params):

# read API keys
	with open('config_secret.json') as cred:
    	     creds = json.load(cred)
             auth = Oauth1Authenticator(**creds)
             client = Client(auth)

	request = client.search_by_coordinates("http://api.yelp.com/v2/search",params=params)
	
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	client.close()
	
	return data
		
def get_search_parameters(lat,long):
	#See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	params["ll"] = "{},{}".format(str(lat),str(long))
	params["radius_filter"] = "2000"
	params["limit"] = "10"

	return params

if __name__=="__main__":
	main()
