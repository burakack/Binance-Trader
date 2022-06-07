import os
import Information
from Indicators import BOLLINGER, RSI, MACDvalue
import Logger
import Tradefuncs
import talib as ta

def bollingertrader():
    global buyprice

    bollinger = BOLLINGER.getBollinger(os.environ['parite'], os.environ['zamandilimi'])
    if os.getenv('didbuy') == "0" and MACDvalue.getMacdValue(os.environ['parite'], os.environ['zamandilimi']) < 0 and \
            float(Information.getprice(os.environ['parite'])) < bollinger[2][-1] \
            and RSI.getRsi(os.environ['parite'], os.environ['zaman']) < 50:

        print("BOT BUYİNG", os.environ['coin'])
        Tradefuncs.al()
        buyprice[0] = float(Information.getprice(os.environ['parite']))
        while buyprice[0] != 0:
            Logger.printinfobollinger()
            if os.getenv('didbuy') == "1" and Information.getprice(os.environ['parite']) > bollinger[2][-1] and buyprice[
                0] > \
                    float(Information.getprice(os.environ['parite'])) * 1.01:
                Tradefuncs.sat()
                print("BOT SELLİNG", os.environ['coin'])
                buyprice[0] = 0
