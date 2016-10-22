#!/usr/bin/python

"""Demonstrates basic usage of the Merchant Data Export API
Base Resource URL: /v3/merchants/{mId}/exports

Script Usage
------------
Update these configuration variables defined in the script body:
- HOST: The target API host
- MERCHANT_ID: The Clover ID of the merchant whose data you want to export
- ACCESS_TOKEN: A valid API token with access to the target merchant
- EXPORT_TYPE: The type of data to export ('ORDERS' or 'PAYMNENTS')
- START_TIME: The start (lower-bound) of the export time window
- END_TIME: The end (upper-bound) of the export time window

$ python ./create_export.py
"""

import requests
import time
import sys
import itertools
import json


# -- Begin Script Configuration --

HOST = 'https://www.clover.com'
MERCHANT_ID = '3S2JC4YEV2XTE'
ACCESS_TOKEN = 'cbb13ad3-14b7-f879-7ab3-1a20ee01c2c2'

EXPORT_TYPE = 'ORDERS'        # "ORDERS" or "PAYMENTS"
START_TIME = '1472688000000'  # 09/15/2016 @ 12:00am (UTC)
END_TIME = '1475193600000'    # 10/15/2016 @ 12:00am (UTC)

# -- End Script Configuration --


SPINNER = itertools.cycle(['|', '/', '-', '\\'])


def main():
    # Request the export
    resp = requests.get(api_url('/v3/merchants/' + MERCHANT_ID))
    print resp.json()
    
    export = create_export(
        export_type=EXPORT_TYPE,
        start_time=START_TIME,
        end_time=END_TIME,
    )
    # print_export(export, 'Requested Export')

    # # Wait for the export to finish processing
    # export = wait_for_export(export['id'])
    # print_export(export, 'Finished Export')

    # # Get the URLs for the exported data
    # export_urls = get_export_urls(export['id'])
    # print_export_urls(export_urls)

    # # Download the data from the export URLs
    # download_exported_data(export_urls)


def create_export(export_type, start_time, end_time):
    """Request a new export"""
    url = api_url('/v3/merchants/' + MERCHANT_ID)

    payload = {
        'type': export_type,
        'startTime': start_time,
        'endTime': end_time,
    }
    # print payload
    resp = requests.get(url)
    # resp = requests.post(url, json=payload)
    resp.raise_for_status()
    print resp
    return resp.json()


def get_export(export_id):
    """Get the current state of the specified export"""
    url = api_url('/v3/merchants/' + MERCHANT_ID + '/exports/' + export_id)

    resp = requests.get(url)
    resp.raise_for_status()

    return resp.json()


def wait_for_export(export_id):
    """Block until the export is finished being processed"""
    while True:
        # Get the current export state
        export = get_export(export_id)

        # If the export is finished, stop waiting
        if export['status'] not in ('PENDING', 'IN_PROGRESS'):
            print_export_status(export, True)
            break

        # If the export is not finished, sleep for a bit
        print_export_status(export)
        time.sleep(.25)

    return export


def get_export_urls(export_id):
    """Extract the export URLs from the specified export"""
    export = get_export(export_id)
    return [u['url'] for u in export['exportUrls']['elements']]


def download_exported_data(export_urls):
    """Download the exported data from the export URLs"""
    print 'Downloaded Data'
    print '---------------'

    for export_url in export_urls:
        resp = requests.get(export_url)
        resp.raise_for_status

        downloaded = resp.json()['elements']

        # For the purposes of this demonstration, just print out the count.
        # In a real application, we would commit this data to some persistent
        # data store.
        count = len(downloaded)
        print 'Downloaded: {}'.format(count)

    print ''


def api_url(resource_path):
    """Generate the URL for an API call"""
    return '{}{}?access_token={}'.format(
        HOST,
        resource_path,
        ACCESS_TOKEN,
    )


def print_export(export, label):
    """Pretty print the export"""
    print ''
    print label
    print '-' * len(label)
    for k, v in export.iteritems():
        if k != 'exportUrls':
            print '{}: {}'.format(k, v)
    print ''


def print_export_status(export, finished=False):
    """Pretty print the export status"""
    spinner = '' if finished else SPINNER.next()
    end = '\n' if finished else '\r'
    print '({}%) Export is {}. {}          {}'.format(
        export['percentComplete'],
        export['status'],
        spinner,
        end,
    ),
    sys.stdout.flush()
    print '\r',


def print_export_urls(export_urls):
    """Pretty print the export URLs"""
    print 'Export URLs'
    print '-----------'

    for export_url in export_urls:
        print export_url
    print ''


if __name__ == '__main__':
    main()