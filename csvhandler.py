import csv
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
    with open('database.csv') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        exists = False
        for row in reader:
            if row[0] == name:
                row[0] = name
                row[1] = price
                exists = True
        if exists == False:
            with open('database.csv', 'a') as output:
                writer = csv.writer(output)
                writer.writerow((name,price))
            return
        '''
        else:
            with open('database.csv', 'r+') as output:
                readers = csv.reader(output)
                writers = csv.writer(output)
                writers.writerow(('dupa', 'dupa'))
                for row in readers:
                    names = row[0]
                    prices = row[1]
                    writers.writerow((names,prices))
                return
            '''

