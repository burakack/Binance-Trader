import os


def takevars():
    f = open('userconfig.txt', 'r')

    text=f.readline()
    text=text[8:].strip()
    os.environ['api_key'] = text

    apisecret=f.readline()
    apisecret=apisecret[11:].strip()
    os.environ['api_secret'] = apisecret

    zamandilimi=f.readline()
    zamandilimi=zamandilimi[12:].strip()
    os.environ['zamandilimi'] = zamandilimi

    coin=f.readline()
    coin=coin[5:].strip()
    os.environ['coin'] = coin

    stable=f.readline()
    stable=stable[7:].strip()
    os.environ['stable'] = stable

    os.environ['parite'] = coin+stable
    f.close()


