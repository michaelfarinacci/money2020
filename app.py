import flask
import json
import os
from flask import Flask, Response, jsonify, request
from sqlalchemy import create_engine, asc, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import app, Merchant, Transactions
#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')
if os.uname()[0] == 'Darwin':
    ip = '52.36.203.109:5432'
else:
    ip = 'localhost'
DBSession = sessionmaker(bind=create_engine('postgresql://postgres:postgres@%s/angel_db_3' % ip))
session = DBSession()

from yelp_session import YelpSession
ys = YelpSession()

def resp(data=""):
    """Create response data json"""
    data = {'data': data}
    return json.dumps(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    version_id =  session.query(Transactions).order_by(Transactions.id.desc()).first().id
    return flask.render_template('index.html', version_id=version_id)

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    transactions = session.query(Transactions).limit(10)
    version_id =  session.query(Transactions).order_by(Transactions.id.desc()).first().id
    if transactions:
        return flask.render_template('transactions.html', transactions = transactions, version_id = version_id)
    else:
        return flask.render_template('transactions.html')

@app.route('/trends', methods=['GET', 'POST'])
def trends():
    version_id =  session.query(Transactions).order_by(Transactions.id.desc()).first().id
    return flask.render_template('trends.html', version_id = version_id)

@app.route('/version', methods=['GET'])
def version():
    record = session.query(Transactions).order_by(Transactions.id.desc()).first()
    data = { 'version_id': record.id }
    return json.dumps(data)


@app.route('/consumer', methods=['GET', 'POST'])
def consumer():
    return flask.render_template('consumer.html')

@app.route('/yelpInfo', methods=['GET', 'POST'])
def get_yelp_info():
    data = ys.get_business_info('Original Gravity', 'San Jose, CA')
    return resp(data)

@app.route('/yelpSales', methods=['GET', 'POST'])
def get_yelp_sales():
    pass

@app.route('/yelpCoordinates', methods=['GET', 'POST'])
def get_yelp_coordinates():
    data = ys.get_coordinate_list('Original Gravity', 'San Jose, CA')
    return resp(data)

#@app.route('/test')
#def test():
#    data = resp("This is the loyalty server!")
#    return Response(response=data, status=200, mimetype="application/json")

if __name__ == '__main__':
    #context = ('server.crt', 'server.key')
    #app.run(host='127.0.0.1', ssl_context=context, threaded=True, debug=True)
    app.run(debug=True, host='10.0.0.164')#, ssl_context=context)
