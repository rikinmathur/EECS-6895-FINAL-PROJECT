import requests
from bs4 import BeautifulSoup
import numpy as np
urleasy="http://www.yelp.com/biz/cable-car-museum-san-francisco"
#reviewcount=0
#while (reviewcount <= 60):
    #url="http://www.yelp.com/biz/cable-car-museum-san-francisco%d" %reviewcount
r = requests.get(urleasy)
soup = BeautifulSoup(r.content)	
#tatti_list=[]

links = soup.find_all("span", {"itemprop": "reviewCount"})

for link in links:
    print link.getText()
    #reviewcount = reviewcount + 20
#np.savetxt ('./%s.txt'%tag.string, np.array(tatti_list),delimiter='\n',fmt = "%s")       