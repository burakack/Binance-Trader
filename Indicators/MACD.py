import time
import datetime as DT
import numpy as np
# pip install pandas
import pandas as pd
# pip install python-binance
from binance.client import Client
from binance.enums import *
import os


client = Client(os.getenv('api_key'), os.getenv('api_secret'))

## tradepair like BTCUSDT,IOTAUSDT time is
def getMacd(tradePair,time):
    klines = client.get_klines(symbol=tradePair, interval=time, limit=500)
    closeVal = [float(entry[4]) for entry in klines]
    closeVal = pd.DataFrame(closeVal)
    ema12 = closeVal.ewm(span=12).mean()
    ema26 = closeVal.ewm(span=26).mean()
    macd = ema26 - ema12
    signal = macd.ewm(span=9).mean()

    macd = macd.values.tolist()
    signal = signal.values.tolist()

    if macd[-1] > signal[-1] and macd[-2] < signal[-2]:
        macdIndicator = 'SELL'
    elif macd[-1] < signal[-1] and macd[-2] > signal[-2]:
        macdIndicator = 'BUY'
    else:
        macdIndicator = 'HOLD'

    return macdIndicator
