import datetime as DT
import time
import numpy as np
# pip install pandas
import pandas as pd
# pip install python-binance
import os
from binance.client import Client
from binance.enums import *

client = Client(os.getenv('api_key'), os.getenv('api_secret'))

def getprice(parite):
    price = client.get_ticker(symbol=parite)
    coiprice = format(float(price['askPrice']), '.4f')
    return coiprice

def getbalance(coin):
    balance = client.get_asset_balance(coin)
    return balance