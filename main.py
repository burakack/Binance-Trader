import Logger
import Envmanager
import os

import Tradefuncs
from Indicators import MACDvalue
from TradeStrategies import Bollingertrader
import Databasemanager
import os
Envmanager.takevars()
Envmanager.nextcoin()
if not os.path.exists('crypto.db'):
    Databasemanager.migration()
Databasemanager.insertcoins()
Databasemanager.incraselosscount()
Databasemanager.incraseprofitcount()
Databasemanager.incraseprofitcount()
Databasemanager.incraseprofitcount()
while True:
    Logger.printinfo()
    Envmanager.nextcoin()




