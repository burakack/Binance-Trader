import time
import datetime as DT
import numpy as np
# pip install pandas
import pandas as pd
# pip install python-binance
import os
import talib as ta
from binance.client import Client
from binance.enums import *

client = Client(os.getenv('api_key'), os.getenv('api_secret'))


def getRsi(tradePair, time):
    klines = client.get_klines(symbol=tradePair, interval=time, limit='500')
    close = [float(entry[4]) for entry in klines]
    close_array = np.array(close)
    rsi = ta.RSI(close_array, timeperiod=14)
    return rsi[-1]
