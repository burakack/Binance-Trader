import os
from datetime import time

import Information
from Indicators import BOLLINGER, RSI, MACDvalue ,MACD
import Logger
import Tradefuncs
import talib as ta

def TDseqtrader():
    global buyprice