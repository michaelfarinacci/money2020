import requests
import time
import sys
import itertools
import json


# Dev credentials:
# HOST = 'https://sandbox.dev.clover.com'
# MERCHANT_ID = '228MVH5XY9JSW'
# ACCESS_TOKEN = '73aef461-c4ac-8245-30d9-2692bc8df623'

# Production credentials:
HOST = 'https://www.clover.com'
ACCESS_TOKEN = 'cbb13ad3-14b7-f879-7ab3-1a20ee01c2c2'
MERCHANT_ID = 'X3VKHK671W7B4'


CUSTOMER_ID = 'W5SG4957ECB7Y'
CUSTOMER_INFO = {
	'firstName': 'Agnieszka',
	'lastName': 'Szefer',
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

ORDER_INFO = {
	'payments': [
		{
			'amount': 10,
			"cardTransaction": {
		        "last4": "0119",
		        "first6": "541333",
		        # "vaultedCard": {
		          # "last4": "0119",
		          # "cardholderName": "TEST/CARD",
		          # "first6": "541333",
		          # "expirationDate": "12/18",
		        # },
		        "cardholderName": "TEST/CARD",
		        "result": "SUCCESS",
		        "avsResult": "SUCCESS"
      		},
      		"device": {
		        "id": ""
		    },
		}
	],
	'authorizations': [],
	# "createdTime": None,
	 "customers": [
	 	{
	 		'id': 'W5SG4957ECB7Y',
	 	}
	],
	"device": {
    	"id": ""
  	},
}

def api_url(resource_path):
    """Generate the URL for an API call"""
    return '{}{}?access_token={}'.format(
        HOST,
        resource_path,
        ACCESS_TOKEN,
    )

def api_with_expand(resource_path):
    """Generate the URL for an API call"""
    return '{}{}&access_token={}'.format(
        HOST,
        resource_path,
        ACCESS_TOKEN,
    )


# MERCHANT ENDPOINTS
def get_merchant_info(merchant_id):
	url = api_url('/v3/merchants/' + merchant_id + '?expand=orders')
	print "Getting info about merchant with id: %s" % merchant_id
	resp = requests.get(url)
	print "Got info about merchant: "
	json_response = resp.json()
	print json_response
	return json_response


def get_merchant_order_ids(merchant_id):
	url = api_with_expand('/v3/merchants/' + merchant_id + '?expand=orders')
	# print "Getting info about merchant with id: %s" % merchant_id
	resp = requests.get(url)
	# print "Got info about merchant: "
	json_response = resp.json()
	# print json_response

	response = json.loads(resp.text)
	orders = response['orders']['elements']
	order_ids = []
	for order in orders:
		order_ids.append(order['id'])

	print order_ids
	return order_ids

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


# def get_customer_info(merchant_id, customer_id, order_id=None):
# 	url = api_url('/v3/merchants/' + merchant_id + '/customers/' + customer_id)

# 	resp = requests.get(url, data=json.dumps(customer_info))

# 	print "Got customer for merchant:"
# 	json_response = resp.json()
# 	print json_response
# 	return json_response


def update_customer(merchant_id, customer_id, customer_info):
	url = api_url('/v3/merchants/' + merchant_id + '/customers/' + customer_id)
	print "Updating a customer for merchant..."
	resp = requests.get(url, data=json.dumps(customer_info))
	print "Updated customer for merchant:"
	json_response = resp.json()
	print json_response
	return json_response


# def create_payment(merchant_id, device_id, order_id):


def create_order(merchant_id, order_info):
	url = api_url('/v3/merchants/' + merchant_id + '/orders')
	print "Creating an order for merchant..."
	resp = requests.post(url, data=json.dumps(order_info))
	print "Created an order for merchant:"
	json_response = resp.json()
	print json_response
	return json_response


def get_order_info(merchant_id, order_id):
	url = api_with_expand('/v3/merchants/' + merchant_id + '/orders/' + order_id + '?expand=customers,payments')
	resp = requests.get(url)
	json_response = resp.json()
	print json_response
	return json_response


if __name__ == '__main__':
    # get_merchant_order_ids(MERCHANT_ID)
    # print
    # get_merchant_orders(MERCHANT_ID)
    # print 
    # get_all_merchant_payments(MERCHANT_ID)
    # print 
    # get_all_merchant_customers(MERCHANT_ID)
    # print 
    # # create_customer_for_merchant(MERCHANT_ID, CUSTOMER_INFO)
    # update_customer(MERCHANT_ID, CUSTOMER_ID, CUSTOMER_INFO)
    # print

    # # get_customer_info(MERCHANT_ID, CUSTOMER_ID)
    # print 

    # create_order(MERCHANT_ID, ORDER_INFO)
    # print 
    get_order_info(MERCHANT_ID, 'T8RBC72172BWC')



    
