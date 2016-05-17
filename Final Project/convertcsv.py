import csv

with open('placesdata.txt',"rb") as infile, open('placesdata.csv','wb') as outfile:
        in_txt = csv.reader(infile, delimiter=',')
        out_csv = csv.writer(outfile)
        out_csv.writerows(in_txt)
