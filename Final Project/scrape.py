import requests
from bs4 import BeautifulSoup
import numpy as np

f=open('testingrest.txt','r')

def remSpace(stri):
    l=[]                
    for elem in stri.split(' '):
            if elem.isalnum():
                    l.append("%s "%elem)
    for idx,charc in enumerate(stri):
        try:            
            if charc == l[0][0]:
                    #print stri[idx:]
                    break
        except:
            pass
    return stri[idx:]

while True:
    urlread=f.readline()
    if not urlread:break
    
    if urlread != "\n":
        x = requests.get(urlread)
        soup = BeautifulSoup(x.content)	   
        
        poops = soup.find_all("span", {"itemprop": "reviewCount"})
        
        for poop in poops:
            num_reviews=poop.getText()
            
        max = 60 if num_reviews>60 else num_reviews    
        reviewcount=0
        tatti_list = []
        
        while (reviewcount <= max):
            url=urlread+"?start=%d" %reviewcount
            r = requests.get(url)
            soup = BeautifulSoup(r.content)
            
            if reviewcount == 0:
                pools = soup.find_all("div",{"class":"biz-page-header-left"})
                for pool in pools:
                    tag_string = remSpace(pool.find('h1').getText())
            links = soup.find_all("div", {"class": "review-content"})
            
            for link in links:
                tatti_list.append(link.find('p').getText())
            reviewcount = reviewcount + 20
        
        np.savetxt ('./%s.txt'%tag_string, np.array(tatti_list),delimiter='\n',fmt = "%s")       