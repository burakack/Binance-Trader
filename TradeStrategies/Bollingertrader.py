import os
import Information
from Indicators import BOLLINGER, RSI, MACDvalue,MACD
import Logger
import Tradefuncs
import talib as ta

def bollingertrader():
    global buyprice

    bollinger = BOLLINGER.getBollinger(os.environ['parite'], os.environ['zamandilimi'])
    if os.getenv('didbuy') == "0" and MACD.getMacd(os.environ['parite'], os.environ['zamandilimi']) == "BUY" and \
            float(Information.getprice(os.environ['parite'])) < bollinger[1][-1] \
            and RSI.getRsi(os.environ['parite'], os.environ['zamandilimi']) < 50:

        print("BOT BUYİNG", os.environ['coin'])
        #Tradefuncs.al()
        buyprice = float(Information.getprice(os.environ['parite']))
        while buyprice != 0:
            Logger.printinfobollinger()
            if os.getenv('didbuy') == "1" and Information.getprice(os.environ['parite']) > bollinger[1][-1] and buyprice\
                    > float(Information.getprice(os.environ['parite'])) * 1.01:
                #Tradefuncs.sat()
                print("BOT SELLİNG", os.environ['coin'])
                buyprice0 = 0
