import flask
import json
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response, jsonify, request
from sqlalchemy import create_engine, asc, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import Transactions
#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@52.36.203.109:5432/angel_db'
db = SQLAlchemy(app)

DBSession = sessionmaker(bind=create_engine('postgresql://postgres:postgres@52.36.203.109:5432/angel_db'))
session = DBSession()

def resp(data=""):
    """Create response data json"""
    data = {'data': data}
    return json.dumps(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    transactions = session.query(Transactions).order_by(asc(Transactions.date))
    if transactions:
        return flask.render_template('transactions.html', transactions = transactions)
        

@app.route('/trends', methods=['GET', 'POST'])
def trends():
    return flask.render_template('trends.html')

#@app.route('/test')
#def test():
#    data = resp("This is the loyalty server!")
#    return Response(response=data, status=200, mimetype="application/json")

if __name__ == '__main__':
    #context = ('server.crt', 'server.key')
    #app.run(host='127.0.0.1', ssl_context=context, threaded=True, debug=True)
    app.run(debug=True, host='127.0.0.1')#, ssl_context=context)
