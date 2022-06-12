import os


def takevars():
    f = open('userconfig.txt', 'r')

    text = f.readline()
    text = text[8:].strip()
    os.environ['api_key'] = text

    apisecret = f.readline()
    apisecret = apisecret[11:].strip()
    os.environ['api_secret'] = apisecret

    zamandilimi = f.readline()
    zamandilimi = zamandilimi[12:].strip()
    os.environ['zamandilimi'] = zamandilimi

    coin = f.readline()
    coin = coin[5:].strip()
    os.environ['coin'] = coin

    stable = f.readline()
    stable = stable[7:].strip()
    os.environ['stable'] = stable

    os.environ['parite'] = coin + stable
    f.close()


    os.environ['didbuy'] = '0'

def nextcoin():
    coinsayisi=1
    f = open('coins.txt', 'r')
    coin = f.readline()
    coin = coin[0:].strip()
    if(coin == os.environ['coin']):
        coinsayisi+=1
        coin = f.readline()
        coin = coin[0:].strip()
        os.environ['coin'] = coin
        os.environ['parite'] = os.environ['coin'] + os.environ['stable']
        os.environ['coinsayisi'] = str(coinsayisi)
        return 1
    while coin != os.environ['coin']:
        coinsayisi += 1
        coin = f.readline()
        coin = coin[0:].strip()
    coinsayisi += 1
    coin = f.readline()
    coin = coin[0:].strip()
    if not coin:
        coinsayisi -= 1
        f.close()
        c = open('coins.txt', 'r')
        coin = c.readline()
        coin = coin[0:].strip()
        os.environ['coin'] = coin
        os.environ['parite'] = os.environ['coin'] + os.environ['stable']
        c.close()
        os.environ['coinsayisi']=str(coinsayisi)
        return 1
    os.environ['coin'] = coin
    os.environ['parite'] = os.environ['coin'] + os.environ['stable']
    f.close()
    os.environ['coinsayisi'] = str(coinsayisi)
    return 1
