from flask import Flask, request
import csvhandler
app = Flask(__name__)

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
