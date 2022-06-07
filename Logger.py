from datetime import datetime
from Indicators import RSI, MACD, MA,MACDvalue,BOLLINGER
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
    BBANDS= BOLLINGER.getBollinger(os.getenv('parite'), os.getenv('zamandilimi'))
    ma50 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 50)
    ma100 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 100)
    ma200 = MA.getMa(os.getenv('parite'), os.getenv('zamandilimi'), 200)
    data = [[os.getenv('parite'), rsi,macd, macdValue,BBANDS[0][-1],BBANDS[1][-1],BBANDS[2][-1], ma50, ma100, ma200 ,price]]
    clear()
    printdate()
    print(tabulate(data, headers=["Parite", "RSI", "MACD","MACDVALUE" ,"BUP","BMİD","BDOWN","MA50", "MA100", "MA200","PRİCE"]))

def printinfobollinger():
    macdValue = MACDvalue.getMacdValue(os.getenv('parite'), os.getenv('zamandilimi'))
    rsi = RSI.getRsi(os.getenv('parite'), os.getenv('zamandilimi'))
    price = Information.getprice(os.getenv('parite'))
    BBANDS = BOLLINGER.getBollinger(os.getenv('parite'), os.getenv('zamandilimi'))
    data = [
        [os.getenv('parite'), format(macdValue[-1], ".4f"), BBANDS[0][-1], BBANDS[1][-1], BBANDS[2][-1], price]]
    clear()
    printdate()
    print(tabulate(data,headers=["Parite", "RSI", "MACDVALUE", "BUP", "BMİD", "BDOWN", "PRİCE"]))

