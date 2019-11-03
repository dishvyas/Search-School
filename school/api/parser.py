import csv
import json
from json2table import convert
# csvfile = open('Bangalore_schools.csv', 'r')
# jsonfile = open('Bangalore_schools.json', 'w')
# fieldnames = ("district","block","cluster","schoolid","schoolname","category","gender","medium_of_inst","address","area","pincode","landmark","identification1","busroutes","identification2","latlong")
# reader = csv.DictReader( csvfile, fieldnames)
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write('\n')
# print("Done")
# data = open('Bangalore_schools.json','r')
# jsonFile = data.read()

table = []
with open('Bangalore_schools.json', 'r') as f:
    for line in f:
        try:
            j = line.split('|')[-1]
            table.append(json.loads(j))
        except ValueError:
            continue
for row in table:
    print(row)
print("Done")

