from flask import Flask, request, Response
import shutil
from launcher import flaskrun
from flask_basicauth import BasicAuth
import csvhandler
import json
from flask_api import status


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

basic_auth = BasicAuth(app)

@app.route('/cake', methods=['DELETE'])
@basic_auth.required
def cake_delete():
    name = request.form['name']
    if csvhandler.search_in_csv(name) == True:
        csvhandler.delete_from_csv(name)
        return "Record found, deleting", status.HTTP_200_OK
    else:
        return "No record found", status.HTTP_400_BAD_REQUEST

@app.route('/cake', methods=['PUT'])
@basic_auth.required
def cake_put():
    name = request.form['name']
    price = request.form['price']
    if csvhandler.search_in_csv(name) == True:
        csvhandler.write_to_csv(name, price)
        return "Record found, changing", status.HTTP_200_OK
    else:
        return "No record found", status.HTTP_400_BAD_REQUEST

@app.route('/cake', methods=['POST'])
@basic_auth.required
def cake_post():
    content = request.get_json()
    
    name = content['name']
    price = content['price']

    data = {'name': name, 'price': price}
    print name
    print price
    csvhandler.write_to_csv(name, price)
    return "Added or modified record", status.HTTP_200_OK

@app.route('/cake', methods=['GET'])
def cake():
    data = csvhandler.read_from_csv(True)
    return data, status.HTTP_200_OK

@app.route('/ekac', methods=['GET'])
def ekac():
    data = csvhandler.read_from_csv(False)
    return data, status.HTTP_200_OK

@app.route('/cake/clear', methods=['GET'])
@basic_auth.required
def cake_clear():
    shutil.copy('database.csv', 'database_old.csv')
    return "Cleared", status.HTTP_200_OK

@app.route('/cake/save', methods=['GET'])
@basic_auth.required
def cake_save():
    shutil.copy('database_old.csv', 'database.csv')
    return "Saved", status.HTTP_200_OK

shutil.copy('database.csv', 'database_old.csv')
flaskrun(app)
