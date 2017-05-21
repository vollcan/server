from flask import Flask, request
app = Flask(__name__)

@app.route('/cake', methods=['GET', 'POST', 'DELETE', 'PUT'])
def cake():
    if request.method=='POST':
        return "This is %s" % request.form['name']
    if request.method=='GET':
        return "This is get cake"
    if request.method=='DELETE':
        return "This is delete cake"
    if request.method=='PUT':
        return "This is put cake"

@app.route('/ecak')
def ekac():
    return "This is ekac"

if __name__=='__main__':
    app.run(debug=True)
