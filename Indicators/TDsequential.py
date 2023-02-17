import Logger
import Envmanager
from Indicators import MACDvalue
from TradeStrategies import Bollingertrader
import os
import sqlite3


def calculatetdseq(values):
    buycount = 1
    sellcount = 0

    for i in range(len(values)):
        t = i-4
        if i-4 < 0:
            t = 0
        if buycount != 0:
            if values[i] > values[t]:
                if buycount == 9:
                    buycount = 1
                    sellcount = 0
                    continue
                buycount += 1
                sellcount = 0
            else:
                sellcount += 1
                buycount = 0
        elif sellcount != 0:
            if values[i] < values[t]:
                if sellcount == 9:
                    sellcount = 1
                    buycount = 0
                    continue
                sellcount += 1
                buycount = 0
            else:
                buycount += 1
                sellcount = 0
    return buycount, sellcount
