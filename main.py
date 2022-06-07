import Logger
import Envmanager
from Indicators import MACDvalue
from TradeStrategies import Bollingertrader
import os
Envmanager.takevars()
while True:
    #Logger.printinfo()
    Bollingertrader.bollingertrader()
    Envmanager.nextcoin()



