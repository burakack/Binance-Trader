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

    # line count in coin.txt
    count = ""
    c = open('userconfig.txt', 'r')
    with c as fp:
        for line in fp:
            if line.strip():
                count += "a"
    c.close()
    os.environ['coinsayisi'] = count
    os.environ['coinindex'] = 'a'
    os.environ['didbuy'] = '0'

def nextcoin():
    f = open('coins.txt', 'r')
    coin = f.readline()
    coin = coin[0:].strip()
    if(coin == os.environ['coin']):
        coin = f.readline()
        coin = coin[0:].strip()
        os.environ['coin'] = coin
        os.environ['parite'] = os.environ['coin'] + os.environ['stable']
        return 1
    while coin != os.environ['coin']:
        coin = f.readline()
        coin = coin[0:].strip()
    coin = f.readline()
    coin = coin[0:].strip()
    if not coin:
        f.close()
        c = open('coins.txt', 'r')
        coin = c.readline()
        coin = coin[0:].strip()
        os.environ['coin'] = coin
        os.environ['parite'] = os.environ['coin'] + os.environ['stable']
        c.close()
        return 1
    os.environ['coin'] = coin
    os.environ['parite'] = os.environ['coin'] + os.environ['stable']
    f.close()
    return 1
