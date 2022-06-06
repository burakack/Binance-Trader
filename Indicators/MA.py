import time
import datetime as DT
import numpy as np
# pip install pandas
import pandas as pd
# pip install python-binance
from binance.client import Client
import talib as ta
from binance.enums import *
import os

client = Client(os.getenv('api_key'), os.getenv('api_secret'))

## tradepair like BTCUSDT,IOTAUSDT time is
def getMa(tradePair,time,zaman):
    klines = client.get_klines(symbol=tradePair, interval=time, limit=zaman)
    closeVal = [float(entry[4]) for entry in klines]
    closeVal = np.array(closeVal)
    ma=ta.MA(closeVal,zaman)
    return ma[-1]
