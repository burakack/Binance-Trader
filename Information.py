import os
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