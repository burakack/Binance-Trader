import time
import datetime as DT
import numpy as np
# pip install pandas
import pandas as pd
# pip install python-binance
from binance.client import Client
from binance.enums import *

api_key = 'tn6TO4lHWLSh2ft3F10ywvg2naV5v88ppBYWfVsfp9XDfmWNrqPXSy8Kt8xC92zv'
api_secret = 'hg7fItAdSanNoHWTthEfzBH5bxjPJz1QwEKZyrQjZIVEcY0g871xAvtEC5Yee0s2'
client = Client(api_key, api_secret)

def getRsi(tradePair,time):
    klines = client.get_klines(symbol=tradePair, interval=time, limit='500')
    close = [float(entry[4]) for entry in klines]
    close_array = np.asarray(close)
    close_finished = close_array[:-1]

    diff = np.diff(close_finished)
    up_chg = 0 * diff
    down_chg = 0 * diff

    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[diff > 0]

    # down change is equal to negative difference, otherwise equal to zero
    down_chg[diff < 0] = diff[diff < 0]

    up_chg = pd.DataFrame(up_chg)
    down_chg = pd.DataFrame(down_chg)

    up_chg_avg = up_chg.ewm(com=13, min_periods=14).mean()
    down_chg_avg = down_chg.ewm(com=13, min_periods=14).mean()

    rs = abs(up_chg_avg / down_chg_avg)
    rsi = 100 - 100 / (1 + rs)
    rsi = int(rsi[0].iloc[-1])
    return rsi