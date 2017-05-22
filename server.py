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
        return
    if request.method=='PUT':
        return

@app.route('/cake')
def cake():
    if request.method=='GET':
        data = csvhandler.csvRead(True)
        return str(data)

@app.route('/ekac')
def ekac():
    return str(csvhandler.csvRead(False))

flaskrun(app)
