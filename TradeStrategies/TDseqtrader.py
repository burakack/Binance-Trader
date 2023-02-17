import os
from datetime import time
import Databasemanager
import Information
from Indicators import BOLLINGER, RSI, MACDvalue, MACD
import Logger
import Tradefuncs
import talib as ta


def TDseqtrader():
    global buyprice
    data15m = Databasemanager.gettdseq(os.environ['coin'], "15m")
    data1h = Databasemanager.gettdseq(os.environ['coin'], "1h")
    data4h = Databasemanager.gettdseq(os.environ['coin'], "4h")
    Logger.printdate()
    if os.getenv('didbuy') == "0" and data15m[0] == 1 and data15m[1] == 3 and data1h[0] == 1 and data4h[0] == 1 and Information.precandlecolor(os.environ['parite'], "15m") == "green" and RSI.getRsi(os.environ['parite'], "15m") < 67:
        os.environ['didbuy'] = "1"
        print("BOT BUYİNG", os.environ['coin'], "PRICE=",
              Information.getprice(os.environ['parite']))
        # Tradefuncs.al()
        buyprice = float(Information.getprice(os.environ['parite']))
        while buyprice != 0:
            if os.getenv('didbuy') == "1" and (
                    float(Information.getprice(os.environ['parite'])) >= buyprice * 1.016 or (data15m[0] == 0 and data15m[1] > 1) or (
                    data15m[0] == 1 and data15m[1] > 7 and float(
                    Information.getprice(os.environ['parite'])) >= buyprice * 1.001)):
                # Tradefuncs.sat()
                if float(Information.getprice(os.environ['parite'])) > buyprice:
                    Databasemanager.incraseprofitcount()
                else:
                    Databasemanager.incraselosscount()
                print("BOT SELLİNG", os.environ['coin'], "PRICE=", Information.getprice(
                    os.environ['parite']))
                buyprice = 0
                os.environ['didbuy'] = "0"
