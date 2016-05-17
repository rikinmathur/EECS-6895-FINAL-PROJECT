import math
from textblob import TextBlob as tb
import os
bloblist=[]

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1.0 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    sc = tf(word, blob) * idf(word, bloblist)
    print  "%s:%f"   %(word,sc)
    return sc
    
with open('placesnames.txt','r') as nameslist:
    names_rikin = nameslist.read().split('\n')
    names_rikin.pop()
    
path = "/home/bigdata/BIG_DATA_PROJECT/yelp-1.0.1/yelp/reviews"
dirs = os.listdir(path)
print dirs
#with open("sentimentdata.txt","a") as writingfile:
for xfile in dirs[:2]:
    file_name = "reviews/%s"%xfile
    with open(file_name,"rb") as f:
        text = f.read()     
        blob=tb(unicode(text, errors='replace'))
        bloblist.append(blob)
        #print bloblist
      
for i, blob in enumerate(bloblist):
    print("Top words in document %s"%names_rikin[i])
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word in sorted_words[:3]:
        print("\tWord: {}".format(word))  
           