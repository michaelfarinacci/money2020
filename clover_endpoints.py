import requests
import time
import sys
import itertools
import json


HOST = 'https://www.clover.com'
MERCHANT_ID = 'X3VKHK671W7B4'
ACCESS_TOKEN = 'cbb13ad3-14b7-f879-7ab3-1a20ee01c2c2'


CUSTOMER_ID = 'W5SG4957ECB7Y'
CUSTOMER_INFO = {
	'firstName': 'Agnieszka',
	'lastName': 'Szefer',
	# 'emailAddresses': ['agnieszka.m.szefer@gmail.com'],
	'cards': [
		{
		  "last4": '0119',
		  "firstName": "TEST",
		  "lastName": "CARD",
		  "first6": "541333",
		  "expirationDate": "12/18",
		}
	],
	'marketingAllowed': True,
}


def api_url(resource_path):
    """Generate the URL for an API call"""
    return '{}{}?access_token={}'.format(
        HOST,
        resource_path,
        ACCESS_TOKEN,
    )

# MERCHANT ENDPOINTS
def get_merchant_info(merchant_id):
	url = api_url('/v3/merchants/' + merchant_id)
	print "Getting info about merchant with id: %s" % merchant_id
	resp = requests.get(url)
	print "Got info about merchant: "
	json_response = resp.json()
	print json_response
	return json_response


def get_merchant_orders(merchant_id):
	url = api_url('/v3/merchants/' + merchant_id + '/orders')
	print "Getting info about merchant orders..."
	resp = requests.get(url)
	print "Got info about merchant orders: "
	json_response = resp.json()
	print json_response
	return json_response


def get_all_merchant_payments(merchant_id):
	url = api_url('/v3/merchants/' + merchant_id + '/payments')
	print "Getting info about all merchant payments..."
	resp = requests.get(url)
	print "Got info about all merchant payments: "
	json_response = resp.json()
	print json_response
	return json_response


def get_all_merchant_customers(merchant_id):
	url = api_url('/v3/merchants/' + merchant_id + '/customers')
	print "Getting info about all merchant customers..."
	resp = requests.get(url)
	print "Got info about all merchant customers: "
	json_response = resp.json()
	print json_response
	return json_response


# CUSTOMER ENDPOINTS PER MERCHANT
def create_customer_for_merchant(merchant_id, customer_info=None):
	url = api_url('/v3/merchants/' + merchant_id + '/customers')

	print "Creating a customer for merchant..."
	resp = requests.post(url, data=json.dumps(customer_info))
	print "Created customer for merchant:"
	json_response = resp.json()
	print json_response
	return json_response


def update_customer(merchant_id, customer_id=None):
	url = api_url('/v3/merchants/' + merchant_id + '/customers/' + CUSTOMER_ID)
	print "Updating a customer for merchant..."
	resp = requests.post(url, data=json.dumps(CUSTOMER_INFO))
	print "Updated customer for merchant:"
	json_response = resp.json()
	print json_response
	return json_response


if __name__ == '__main__':
    get_merchant_info(MERCHANT_ID)
    print
    get_merchant_orders(MERCHANT_ID)
    print 
    get_all_merchant_payments(MERCHANT_ID)
    print 
    get_all_merchant_customers(MERCHANT_ID)
    print 
    # create_customer_for_merchant(MERCHANT_ID, None)
    update_customer(MERCHANT_ID, CUSTOMER_ID)
    

    
