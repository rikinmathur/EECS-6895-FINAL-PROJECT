from googleplaces import GooglePlaces, types, lang
import urllib, json


YOUR_API_KEY = 'AIzaSyCiUUV45HvFFOYvbVITo65qABlHDNKQT7A'
params={}
request={}
google_places = GooglePlaces(YOUR_API_KEY)



f=open('latdatathree.txt')
while True:
    nameread=f.readline().split('\n')
    if not nameread:break     
    for names in nameread:
        print name.strip().split(",")
        params["name"] = names
        query_result = google_places.nearby_search(location="San Francisco", **params)
        for place in query_result.places[:1]:
                placeid = place.place_id
#
#
#        MyUrl = ('https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s') % (placeid,YOUR_API_KEY)
#          #grabbing the JSON result
#        response = urllib.urlopen(MyUrl)
#        jsonRaw = response.read()
#        jsonData = json.loads(jsonRaw)
#        
#        hourno=str(jsonData).find('Tuesday:')+6
#        myfile.write('\n'+str(jsonData)[hourno:hourno+9]+','+str(jsonData)[hourno+13:hourno+26])
