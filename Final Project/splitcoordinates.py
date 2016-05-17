import numpy as np

filename = open('placesdata.csv','r') 
X = np.loadtxt(filename,delimiter=',',dtype=str)    
lat_lon = X[1:, 1:3]
with open("latdatatwo.txt",'a') as fid:
    lat_lon.tofile(fid, format="%f")

