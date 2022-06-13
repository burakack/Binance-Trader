import os
from binance.client import Client
import datetime


def sat():
    client = Client(os.getenv('api_key'), os.getenv('api_secret'))
    price = client.get_ticker(symbol=os.getenv('parite'))
    balance = client.get_asset_balance(asset=os.getenv('coin'))
    sigNumOfCoin = '.' + str(len(str(int(float(price['askPrice']))))) + 'f'
    coiNumber = format(float(balance['free']), sigNumOfCoin)
    coiprice = format(float(price['askPrice']), '.4f')
    ## SAT
    print(coiNumber, "ADET", os.getenv('coin'), "SATİLİYOR SATİLAN FİYAT: ", coiprice)
    order = client.order_limit_sell(
        symbol=os.getenv('parite'),
        quantity=coiNumber,
        price=coiprice)


def al():
    client = Client(os.getenv('api_key'), os.getenv('api_secret'))
    price = client.get_ticker(symbol=os.getenv('parite'))
    balance = client.get_asset_balance(asset=os.getenv('stable'))
    coiNumber = format(float(balance['free']), '.4f')
    coiprice = format(float(price['askPrice']), '.4f')
    print(coiNumber, "ADET", os.getenv('coin'), "ALİNİYOR SATİLAN FİYAT: ", coiprice)
    order = client.order_limit_buy(
        symbol=os.getenv('parite'),
        quantity=coiNumber,
        price=coiprice)
#stoploss function
def stoploss():
    today = datetime.date.today()
    client = Client(os.getenv('api_key'), os.getenv('api_secret'))
    week_ago = today - datetime.timedelta(days=6)
    week_ago = week_ago.strftime('%d %b, %Y')
    klines2 = client.get_historical_klines(os.environ['parite'], Client.KLINE_INTERVAL_1DAY, str(week_ago))
    highVal = [float(entry[2]) for entry in klines2]
    minval = [float(entry[3]) for entry in klines2]
    close = [float(entry[4]) for entry in klines2]
    avgDownDrop = (sum(highVal)/len(highVal)-sum(minval)/len(minval))/(sum(minval)/len(minval))
    stoploss = close[-2]*(1-avgDownDrop)
    return stoploss