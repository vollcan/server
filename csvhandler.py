import csv, shutil
import json
def read_from_csv(ascending=True):
    with open('database_old.csv') as csvfile:
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
        #jsonlist = json.dumps(sortedlist, sort_keys=True)
    return sortedlist

def write_to_csv(name, price):
    fieldnames = ["name", "price"]
    with open('database_old.csv', 'r') as csvfile, open('buffer.csv', 'w') as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in reader:
            if not name == row['name']:
                writer.writerow({'name': row['name'], 'price': row['price']})
        writer.writerow({'name': str(name), 'price': str(price)})
    shutil.move('buffer.csv','database_old.csv')

def delete_from_csv(name):
    fieldnames = ["name", "price"]
    with open('database_old.csv', 'r') as csvfile, open('buffer.csv', 'w') as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in reader:
            if not name == row['name']:
                writer.writerow({'name': row['name'], 'price': row['price']})
    shutil.move('buffer.csv','database_old.csv')

def search_in_csv(name):
    fieldnames = ["name", "price"]
    with open('database_old.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if name == row['name']:
                return True
        return False
