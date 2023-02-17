import os
from datetime import time

import Information
from Indicators import BOLLINGER, RSI, MACDvalue, MACD
import Logger
import Tradefuncs
import talib as ta


def bollingertrader():
    global buyprice

    bollinger = BOLLINGER.getBollinger(
        os.environ['parite'], os.environ['zamandilimi'])
    Logger.printdate()
    if os.getenv('didbuy') == "0" and MACDvalue.getMacdValue(os.environ['parite'], os.environ['zamandilimi']) < 0 and \
            float(Information.getprice(os.environ['parite'])) < bollinger[2][-1] \
            and RSI.getRsi(os.environ['parite'], os.environ['zamandilimi']) < 50:
        os.environ['didbuy'] = "1"
        print("BOT BUYİNG", os.environ['coin'], "PRICE=",
              Information.getprice(os.environ['parite']))
        # Tradefuncs.al()
        buyprice = float(Information.getprice(os.environ['parite']))
        while buyprice != 0:
            print(buyprice, "=?=", Information.getprice(os.environ['parite']))
            if os.getenv('didbuy') == "1" and float(Information.getprice(os.environ['parite'])) > bollinger[0][-1]:
                # Tradefuncs.sat()
                print("BOT SELLİNG", os.environ['coin'], "PRICE=", Information.getprice(
                    os.environ['parite']))
                buyprice = 0
                os.environ['didbuy'] = "0"
    time.sleep(20)
