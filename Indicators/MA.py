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

## tradepair like BTCUSDT,IOTAUSDT time is
def getMa(tradePair,time,zaman):
    klines = client.get_klines(symbol=tradePair, interval=time, limit=zaman)
    closeVal = [float(entry[4]) for entry in klines]
    toplam= sum(closeVal)
    adet = len(closeVal)
    return toplam/adet


