from datetime import datetime
from Indicators import RSI, MACD, MA,MACDvalue
import Information
from tabulate import tabulate
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def printdate():
    now = datetime.today()
    print(now, " Bot working normally.")


def printinfo():
    macdValue=MACDvalue.getMacdValue(os.getenv('parite'), os.getenv('zamandilimi'))
    rsi = RSI.getRsi(os.getenv('parite'), os.getenv('zamandilimi'))
    macd = MACD.getMacd(os.getenv('parite'), os.getenv('zamandilimi'))
    price = Information.getprice(os.getenv('parite'))
    ma50 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 50)
    ma100 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 100)
    ma200 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 200)
    data = [[os.getenv('parite'), rsi, format(macdValue[0],".4f"), ma50, ma100, ma200 ,price]]
    clear()
    printdate()
    print(tabulate(data, headers=["Parite", "RSI", "MACD","MACDVALUE" , "MA50", "MA100", "MA200","PRİCE"]))
