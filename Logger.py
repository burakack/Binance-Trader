from datetime import datetime
from Indicators import RSI,MACD
import Information
import os
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def printdate():
    now = datetime.today()
    print(now," Bot working normally.")

def printindicators():
    rsi=RSI.getRsi(os.getenv('parite'), os.getenv('zamandilimi'))
    macd=MACD.getMacd(os.getenv('parite'), os.getenv('zamandilimi'))
    info=Information.getprice(os.getenv('parite'))
    print("RSI-MACD-PRİCE")
    print( rsi,macd,info)
