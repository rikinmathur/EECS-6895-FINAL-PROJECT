import csv
import json

csvfile = open('placesdata.csv', 'r')
jsonfile = open('coordinates.json', 'w')

fieldnames = ("PlaceName","Latitude","Longitude","Rating")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')