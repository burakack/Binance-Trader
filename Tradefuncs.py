import datetime as DT
import time
import numpy as np
# pip install pandas
import pandas as pd
# pip install python-binance
import os
from binance.client import Client
from binance.enums import *


def sat():
    client = Client(os.getenv('api_key'), os.getenv('api_secret'))
    price = client.get_ticker(symbol=os.getenv('parite'))
    balance = client.get_asset_balance(asset=os.getenv('coin'))
    sigNumOfCoin = '.' + str(len(str(int(float(price['askPrice']))))) + 'f'
    coiNumber = format(float(balance['free']), sigNumOfCoin)
    coiprice = format(float(price['askPrice']), '.4f')
    ## SAT
    print(coiNumber, "ADET", os.getenv('coin'), "SATİLİYOR SATİLAN FİYAT: ", coiprice)
    order = client.order_limit_sell(
        symbol=os.getenv('parite'),
        quantity=coiNumber,
        price=coiprice)


def al():
    client = Client(os.getenv('api_key'), os.getenv('api_secret'))
    price = client.get_ticker(symbol=os.getenv('parite'))
    balance = client.get_asset_balance(asset=os.getenv('stable'))
    coiNumber = format(float(balance['free']), '.4f')
    coiprice = format(float(price['askPrice']), '.4f')
    print(coiNumber, "ADET", os.getenv('coin'), "ALİNİYOR SATİLAN FİYAT: ", coiprice)
    order = client.order_limit_buy(
        symbol=os.getenv('parite'),
        quantity=coiNumber,
        price=coiprice)