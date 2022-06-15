import os


def takevars():
    f = open('userconfig.txt', 'r')

    name = f.readline()
    name = name[9:].strip()
    os.environ['name'] = name


    api_key = f.readline()
    api_key = api_key[8:].strip()
    os.environ['api_key'] = api_key

    apisecret = f.readline()
    apisecret = apisecret[11:].strip()
    os.environ['api_secret'] = apisecret

    zamandilimi = f.readline()
    zamandilimi = zamandilimi[12:].strip()
    os.environ['zamandilimi'] = zamandilimi

    c = open('coins.txt', 'r')
    coin = c.readline()
    coin = coin[0:].strip()
    os.environ['coin'] = coin
    c.close()

    f.readline()

    stable = f.readline()
    stable = stable[7:].strip()
    os.environ['stable'] = stable

    os.environ['parite'] = coin + stable
    f.close()


    os.environ['didbuy'] = '0'


def calcnumberofcoins():
    with open(r"coins.txt", 'r') as fp:
        num_lines = sum(1 for line in fp)
    os.environ['coinsayisi']=str(num_lines)
    return num_lines

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
