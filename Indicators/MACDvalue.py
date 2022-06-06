
# pip install pandas
import pandas as pd
from binance.client import Client
import os


client = Client(os.getenv('api_key'), os.getenv('api_secret'))

## tradepair like BTCUSDT,IOTAUSDT time is
def getMacdValue(tradePair,time):
    klines = client.get_klines(symbol=tradePair, interval=time, limit=500)
    closeVal = [float(entry[4]) for entry in klines]
    closeVal = pd.DataFrame(closeVal)
    ema12 = closeVal.ewm(span=12).mean()
    ema26 = closeVal.ewm(span=26).mean()
    macd = ema26 - ema12
    macd = macd.values.tolist()
    return macd[-1]
