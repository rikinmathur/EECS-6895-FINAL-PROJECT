
from geopy.distance import vincenty
from geopy.geocoders import Nominatim
import numpy as np
from time import gmtime, strftime
currenttime=float(strftime("%H%M", gmtime()))-700
from flask import Flask, render_template, request
app = Flask(__name__)
#import json

#YOUR_API_KEY = 'AIzaSyCiUUV45HvFFOYvbVITo65qABlHDNKQT7A'
#params={}
#request={}
#google_places = GooglePlaces(YOUR_API_KEY)

lat_array=[]
long_array=[]
dist=[]
indices=[]
final_ratings=[]
openhours=[]
closehours=[]
anand = '0000'
hours=[]   
location=[]
latnew=[]
longnew=[]
contentstring=['','','','','']
#params["name"] = names

#query_result = google_places.nearby_search(location="San Francisco", **params)
#for place in query_result.places[:1]:
#        placeid = place.place_id


@app.route('/my_form_post', methods=['POST'])
def my_form_post():
    a = request.form.get('text')
#    geolocator = Nominatim()
#    location = geolocator.geocode(a,timeout=15)
    input_lat=37.7799335
    input_long=-122.4456705
#    f=open('coordinates.txt')
#    nameread=f.readlines()   
#    for names in nameread:
#        values = names.split("\t")
#        lat_array.append(float(values[0]))
#        long_array.append(float(values[1]))
#        f.close()
#    
#    for i in range(0,len(lat_array)):
#        igor=[lat_array[i],long_array[i]]
#        jigor=[input_lat,input_long]
#        dist.append(vincenty(igor,jigor).meters)
#    
#    indices=np.argsort(dist)
#    
#    for k in range(0,5):
#        i=indices[k]
#        latnew.append(lat_array[i])
#        longnew.append(long_array[i])
#    #br=open('placeshours.txt','r')
#    #poparead=br.readlines()  
#    #for popa in poparead[:23]:
#    #    if popa == '24 hours\n':
#    #        hours[0] = anand
#    #        hours[1]= anand
#    #        openhours.append(float(hours[0]))
#    #        closehours.append(float(hours[1])+2400)
#    #    else:
#    #        hours = popa.split(" ")
#    #        hours[1]=hours[1].rstrip()
#    #        openhours.append(float(hours[0]))
#    #        closehours.append(float(hours[1])+1200)
#    #
#    #for k in range(0,5):
#    #    if openhours[k]>currenttime and closehours[k]>currenttime:
#    #        indices[k]=[]
#    #    else:
#    #        indices[k]=indices[k]
#    #        
#    #fr=open('finalratings.txt','r')
#    #gogaread=fr.readlines()  
#    #for goga in gogaread:
#    #    final_ratings.append(goga)
#    #    
#    #for yo in range(0,len(indices)-1):
#    #    if final_ratings[yo]>final_ratings[yo+1]:
#    #        indices[yo]=indices[yo]
#    #    else:
#    #        indices[yo]=[]
#    #        
    latnew=[37.78374, 37.78573, 37.787682, 37.7827904165, 37.7817745534]
    longnew=[-122.433005, -122.42956, -122.433853, -122.435116768, -122.425714988]
    contentstring[0] = 'The Fillmore SanSan Rating: 3.9'
    contentstring[1] = 'Clay Theatre SanSan Rating: 3.6 https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194'
    contentstring[2] = 'Rose Parks Elem SanSan Rating: 3.6'
    contentstring[3] = 'Roam Artisans Burgers SanSan Rating: 3.3'
    contentstring[4] = 'Starbucks San San Rating: 3.6'    
    return render_template("mappedbitch.html",contentstring=contentstring,latnew=latnew,longnew=longnew)
#
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
