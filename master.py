`#!/usr/bin/env python

import os
import sys
import time
from stockreport import post_stock_price


DEVICE_NAME1 = os.environ.get('DEVICE_NAME', 'stockreport1')
DEVICE_NAME2 = os.environ.get('DEVICE_NAME', 'stockreport2')

APIKEY = os.environ['M2X_API_KEY']

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)


while True:
    print "Posting stock prices."
    # Post stock price of AT&T
    post_stock_price("T", APIKEY, DEVICE_NAME1)
    post_stock_price("A", APIKEY, DEVICE_NAME1)
    print "Stock prices posted." + " DEVICE_NAME1: " + DEVICE_NAME1 + " DEVICE_NAME2: " + DEVICE_NAME2
    time.sleep(60)
