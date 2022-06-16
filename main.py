import Logger
import Envmanager
import os

import Tradefuncs
from Indicators import MACDvalue
from TradeStrategies import TDseqtrader
import Databasemanager
import Updatetdseq
import os

Envmanager.takevars()
Envmanager.nextcoin()
Envmanager.calcnumberofcoins()
if not os.path.exists('crypto.db'):
    Databasemanager.migration()
Databasemanager.insertcoins()
while True:
    Updatetdseq.updatetdseq(os.environ['parite'])
    Logger.printdate()
    TDseqtrader.TDseqtrader()
    Envmanager.nextcoin()




