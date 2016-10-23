import flask
import json
import os
from flask import Flask, Response, jsonify, request
from sqlalchemy import create_engine, asc, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import app, Merchant
#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')
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
    transactions = session.query(Merchant)
    if transactions:
        return flask.render_template('transactions.html', transactions = Merchant)


@app.route('/trends', methods=['GET', 'POST'])
def trends():
    return flask.render_template('trends.html')

@app.route('/consumer', methods=['GET', 'POST'])
def consumer():
    return flask.render_template('consumer.html')


#@app.route('/test')
#def test():
#    data = resp("This is the loyalty server!")
#    return Response(response=data, status=200, mimetype="application/json")

if __name__ == '__main__':
    #context = ('server.crt', 'server.key')
    #app.run(host='127.0.0.1', ssl_context=context, threaded=True, debug=True)
    app.run(debug=True, host='127.0.0.1')#, ssl_context=context)
