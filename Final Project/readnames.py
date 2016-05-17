#!/usr/bin/python

import os
# Open a file
path = "/home/bigdata/BIG_DATA_PROJECT/yelp-1.0.1/yelp/reviews"
dirs = os.listdir(path) 
filetatti_list=[]
filetatti_newlist=[]
# This would print all the files and directories
for file in dirs:
   filetatti_list.append(file.split('\n'))
   for x in filetatti_list:
        os.rename(file,'%s.txt' %x[0])
        
        
        