import Logger
import Envmanager
from Indicators import MACDvalue
from TradeStrategies import Bollingertrader
import os
import sqlite3
from td_sequential_calculator import TDS

t = 0
for i in range(22):
    t += 1
    buy_setup, sell_setup, buy, sell = TDS.price_update(i)
    print(f"Buy setup: {buy_setup}")
    print(f"Sell setup: {sell_setup}")
    if buy:
        print("BUY")
    elif sell:
        print("SELL")
connection = sqlite3.connect('crypto.db')

