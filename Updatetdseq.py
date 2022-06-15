import os
from binance.client import Client
from Indicators.TDsequential import calculatetdseq
import Databasemanager
from td_sequential_calculator import TDS

client = Client(os.getenv('api_key'), os.getenv('api_secret'))


def updatetdseq(Tradepair):
    tdseq15m = 0
    is15mg = 0
    tdseq1h = 0
    is1hg = 0
    tdseq4h = 0
    is4hg = 0

    # calculate for 15m
    klines = client.get_klines(symbol=Tradepair, interval="15m", limit=50)
    closeVal = [float(entry[4]) for entry in klines]
    [buyvalue, sellvalue] = calculatetdseq(closeVal)
    if buyvalue == 0:
        tdseq15m = sellvalue
        is15mg = 0
    else:
        tdseq15m = buyvalue
        is15mg = 1

    # calculate for 1h
    klines = client.get_klines(symbol=Tradepair, interval="1h", limit=50)
    closeVal = [float(entry[4]) for entry in klines]
    [buyvalue, sellvalue] = calculatetdseq(closeVal)
    if buyvalue == 0:
        tdseq1h = sellvalue
        is1hg = 0
    else:
        tdseq1h = buyvalue
        is1hg = 1

    # calculate for 4h
    # calculate for 4h
    klines = client.get_klines(symbol=Tradepair, interval="4h", limit=50)
    closeVal = [float(entry[4]) for entry in klines]
    [buyvalue, sellvalue] = calculatetdseq(closeVal)
    if buyvalue == 0:
        tdseq4h = sellvalue
        is4hg = 0
    else:
        tdseq4h = buyvalue
        is4hg = 1
    Databasemanager.changetdseq(os.environ['coin'], is15mg, tdseq15m, is1hg, tdseq1h, is4hg, tdseq4h)
