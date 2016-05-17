from textblob import TextBlob

import os

path = "/home/bigdata/BIG_DATA_PROJECT/yelp-1.0.1/yelp/reviews"
dirs = os.listdir(path) 
with open('placesnames.txt','r') as nameslist:
    names_rikin = nameslist.read().split('\n')
with open("sentimentdata.txt","a") as writingfile:
    for xfile in dirs:
        file_name = "reviews/%s"%xfile
        with open(file_name,"r") as f:
            text = f.read()     
            text = unicode(text, errors='replace')
            blob = TextBlob(text)
            blob.tags           
            #
            blob.noun_phrases   
            writingfile.write("%f\n\n"%blob.sentiment.polarity)
            