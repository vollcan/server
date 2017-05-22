from flask import Flask, request, Response
from launcher import flaskrun
from flask_basicauth import BasicAuth
import csvhandler
import json
app = Flask(__name__)

#app.config['BASIC_AUTH_USERNAME'] = 'admin'
#app.config['BASIC_AUTH_PASSWORD'] = 'admin'

#basic_auth = BasicAuth(app)

@app.route('/cake', methods=['POST', 'DELETE', 'PUT'])
#@basic_auth.required
def cakeSecret():
    if request.method=='POST':
        content = request.get_json()

        name = content['name']
        price = content['price']

        data = {'name': name, 'price': price}
        print name
        print price
        csvhandler.csvWrite(name, price)
        return str(data)
    if request.method=='DELETE':
        name = request.form['name']
        if csvhandler.csvSearch(name) == True:
            csvhandler.csvDelete(name)
            return "Record found, deleting"
        else:
            return "No record found"
    if request.method=='PUT':
        name = request.form['name']
        price = request.form['price']
        if csvhandler.csvSearch == True:
            csvhandler.csvWrite(name, price)
            return "Record found, changing"
        else:
            return "No record found"

@app.route('/cake')
def cake():
    if request.method=='GET':
        data = csvhandler.csvRead(True)
        return str(data)

@app.route('/ekac')
def ekac():
    return str(csvhandler.csvRead(False))

flaskrun(app)
