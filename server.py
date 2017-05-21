from flask import Flask, request, Response
from flask_basicauth import BasicAuth
import csvhandler
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

basic_auth = BasicAuth(app)

@app.route('/cake', methods=['POST', 'DELETE', 'PUT'])
@basic_auth.required
def cakeSecret():
    if request.method=='POST':
        return
    if request.method=='DELETE':
        return
    if request.method=='PUT':
        return

@app.route('/cake', methods=['GET', 'POST', 'DELETE', 'PUT'])
def cake():
    if request.method=='POST':
        return "This is %s" % request.form['name']
    if request.method=='GET':
        data = csvhandler.csvRead(True)
        return str(data)
    if request.method=='DELETE':
        return "This is delete cake"
    if request.method=='PUT':
        return "This is put cake"

@app.route('/ekac')
def ekac():
    return str(csvhandler.csvRead(False))

if __name__=='__main__':
    app.run(debug=True)
