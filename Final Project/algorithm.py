ratings=[]
sentiment=[]

with open('finalratings.txt','a') as myfile:

    f=open('ratings.txt','r')
    lines= (line.rstrip() for line in f) 
    lines = list(line for line in lines if line)
    for names in lines:
            ratings.append(float(names))
        
    p=open('sentimentdata.txt','r')
    feeds= (koka.rstrip() for koka in p) 
    feeds = list(koka for koka in feeds if koka)
    for feed in feeds:
            sentiment.append((float(feed)*2.5)+2.5)
            
    for i in range(0,len(ratings)):
        myfile.write(str((ratings[i]+sentiment[i])/2.0)+'\n')
    
    