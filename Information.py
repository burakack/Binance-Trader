import os
import numpy as np
# pip install python-binance
from binance.client import Client

client = Client(os.getenv('api_key'), os.getenv('api_secret'))

def getprice(parite):
    price = client.get_ticker(symbol=parite)
    coiprice = format(float(price['askPrice']), '.4f')
    return coiprice

def getbalance(coin):
    balance = client.get_asset_balance(coin)
    return balance

def precandlecolor(tradePair,time):
    klines = client.get_klines(symbol=tradePair, interval=time, limit='10')
    close = [float(entry[4]) for entry in klines]
    close_array = np.array(close)
    if close_array[-3]>close_array[-2]:
        return "red"
    else:
        return "green"