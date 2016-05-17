import requests
from bs4 import BeautifulSoup
import numpy as np
pagecount=0
gdata_list = []
reviewcount=0
string=""
linktext=()

while (reviewcount <= 60):

    url="http://www.yelp.com/search?find_desc=Museums&find_loc=San+Francisco,+CA&start=%d" %reviewcount
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content) 
    pools = soup.find_all("div",{"class":"photo-box pb-90s"})
    for pool in pools:
        with open("test.txt","a") as myfile:
            myfile.write("\nhttp://www.yelp.com"+pool.a['href']+"\n")
    reviewcount = reviewcount + 10


