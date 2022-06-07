import os
import Information
from Indicators import BOLLINGER, RSI, MACDvalue
import Logger
import Tradefuncs


def bollingertrader():
    global buyprice
    buyprice = 0
    bollinger = BOLLINGER.getBollinger(os.environ['parite'], os.environ['zaman'])
    if os.getenv('didbuy') == "0" and MACDvalue.getMacdValue(os.environ['parite'], os.environ['zaman']) <0 and \
            Information.getprice(os.environ['parite']) < bollinger[2] \
            and RSI.getRsi(os.environ['parite'], os.environ['zaman']) < 50:

        print("BOT BUYİNG", os.environ['coin'])
        Tradefuncs.al()
        buyprice = int(Information.getprice(os.environ['parite']))
        while buyprice != 0:
            Logger.printinfobollinger()
            if os.getenv('didbuy') == "1" and Information.getprice(os.environ['parite']) > bollinger[2] and buyprice >\
                    int(Information.getprice(os.environ['parite'])) * 1.01:
                Tradefuncs.sat()
                print("BOT SELLİNG", os.environ['coin'])
                buyprice = 0
