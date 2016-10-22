import requests
import time
import sys
import itertools
import json


HOST = 'https://www.clover.com'
MERCHANT_ID = 'X3VKHK671W7B4'
ACCESS_TOKEN = 'cbb13ad3-14b7-f879-7ab3-1a20ee01c2c2'


def api_url(resource_path):
    """Generate the URL for an API call"""
    return '{}{}?access_token={}'.format(
        HOST,
        resource_path,
        ACCESS_TOKEN,
    )


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


if __name__ == '__main__':
    get_merchant_info(MERCHANT_ID)
    get_merchant_orders(MERCHANT_ID)
    get_all_merchant_payments(MERCHANT_ID)

    
