import csv, shutil
import json
def csvRead(ascending):
    with open('database.csv') as csvfile:
        fieldnames = ['name', 'price']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
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

def csvWrite(name, price):
    fieldnames = ["name", "price"]
    with open('database.csv', 'r') as csvfile, open('buffer.csv', 'w') as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in reader:
            if not name == row['name']:
                writer.writerow({'name': row['name'], 'price': row['price']})
        writer.writerow({'name': str(name), 'price': str(price)})
    shutil.move('buffer.csv','database.csv')

def csvDelete(name):
    fieldnames = ["name", "price"]
    with open('database.csv', 'r') as csvfile, open('buffer.csv', 'w') as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in reader:
            if not name == row['name']:
                writer.writerow({'name': row['name'], 'price': row['price']})
    shutil.move('buffer.csv','database.csv')
