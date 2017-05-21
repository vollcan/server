import csv
import json
def csvRead(ascending):
    with open('database.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        if ascending==True:
            sortedlist = sorted(reader, key=lambda row:(
                        row['name'],row['price']),reverse=False)
        if ascending==False:
            sortedlist = sorted(reader, key=lambda row:(
                        row['name'],row['price']),reverse=True)

        for row in sortedlist:
            print(row['name'], row['price'])
            jsonlist = json.dumps(sortedlist, sort_keys=True)
    return jsonlist

