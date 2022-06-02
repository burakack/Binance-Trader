from datetime import datetime
from Indicators import RSI, MACD, MA
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
    rsi = RSI.getRsi(os.getenv('parite'), os.getenv('zamandilimi'))
    macd = MACD.getMacd(os.getenv('parite'), os.getenv('zamandilimi'))
    price = Information.getprice(os.getenv('parite'))
    ma50 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 50)
    ma100 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 100)
    ma200 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 200)
    data = [[os.getenv('parite'), rsi, macd, ma50, ma100, ma200, price]]
    print(tabulate(data, headers=["Parite", "RSI", "MACD", "MA50", "MA100", "MA200", "PRİCE"]))
