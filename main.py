import time

import Logger
import Trader
from Trader import al,sat
from Indicators import MACD, RSI
import Information
import os
import Envmanager
from datetime import datetime

# pip install pandas
# pip install python-binance


Envmanager.takevars()
while True:
    Logger.printdate()
    Logger.printindicators()
    Trader.al()
    Trader.sat()




