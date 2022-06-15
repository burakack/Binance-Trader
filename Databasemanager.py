import os
import sqlite3
import Envmanager

def migration():
    conn=sqlite3.connect(('crypto.db'))

    c=conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS coins (
                    name text,
                    is15mg int,
                    tdseq15m int,
                    is1hmg int,
                    tdseq1h int,
                    is4hg int,
                    tdseq4h int);
                    """)
    conn.commit()

    c.execute(""" CREATE TABLE IF NOT EXISTS info (
                    name text,
                    money int,
                    tradecount int,
                    profitcount int,
                    losscount int);
                    """)
    conn.commit()
    insertuser(0,0,0,0)
    conn.close()

def insertcoins():
    print("Coins inserting database")
    conn=sqlite3.connect(('crypto.db'))
    c=conn.cursor()
    for i in range(int(os.environ['coinsayisi'])):
        c.execute("SELECT name FROM coins WHERE name='"+os.environ['coin']+"';")
        result=c.fetchone()
        conn.commit()
        if result is None:
            print("Inserted", os.environ['coin'])
            c.execute(" INSERT INTO coins VALUES ('"+os.environ['coin']+"',0,0,0,0,0,0);")
            conn.commit()
        Envmanager.nextcoin()
    conn.close()

def gettdseq(name,time):
    conn=sqlite3.connect(('crypto.db'))

    c=conn.cursor()

    c.execute("SELECT is"+time+"g ,tdseq"+time+" FROM coins WHERE name="+name+");")
    datas=c.fetchone()
    conn.commit()
    conn.close()
    return datas

def changetdseq(name,is15mg,tdseq15m,is1hg,tdseq1h,is4hg,tdseq4h):
    params=(is15mg,tdseq15m,is1hg,tdseq1h,is4hg,tdseq4h,name)
    conn=sqlite3.connect(('crypto.db'))

    c=conn.cursor()
    c.execute('''UPDATE coins SET is15mg=? , tdseq15m=? , is1hmg=? , tdseq1h=? , is4hg=?, tdseq4h=?
     WHERE ?;  ''',params)
    conn.commit()
    conn.close()

def insertuser(money, tradecount, profitcount, losscount):
    print("User inserted!")
    params = (os.environ['name'],money, tradecount, profitcount, losscount )
    conn = sqlite3.connect(('crypto.db'))

    c = conn.cursor()
    c.execute('''INSERT INTO info VALUES (?,?,?,?,?) ''', params)
    conn.commit()
    conn.close()


