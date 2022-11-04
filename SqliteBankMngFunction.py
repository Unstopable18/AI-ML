import datetime
import random
import sqlite3
"""client=sqlite3.connect('BankMng.db')
c=client.cursor()
c.execute("CREATE TABLE acno(_id text,name text,password text,balance text,date text,time text)")
client.commit()"""


def credit(ac):
    client=sqlite3.connect('BankMng.db')
    c=client.cursor()
    c.execute("SELECT * FROM acno where _id = (?)", (ac,))
    data=c.fetchone()
    amt=float(input('Enter amount to be credited:\t'))
    c.execute("UPDATE acno SET balance=balance+(?) where _id = (?)", (amt,ac,))
    client.commit()
    balance(ac)
    client.close()

def debit(ac):
    client=sqlite3.connect('BankMng.db')
    c=client.cursor()
    c.execute("SELECT * FROM acno where _id = (?)", (ac,))
    data=c.fetchone()
    amt=float(input('Enter amount to be debited:\t'))
    bal=float(data[3])
    if(bal>=amt):
        c.execute("UPDATE acno SET balance=balance-(?) where _id = (?)", (amt,ac,))
        client.commit()
        balance(ac)      
    else:
        print('Insufficient Balance!!!')
    client.close()
    
def balance(ac):
    client=sqlite3.connect('BankMng.db')
    c=client.cursor()
    c.execute("SELECT * FROM acno where _id = (?)", (ac,))
    data=c.fetchone()
    print('Balance:\t',data[3])
    client.commit()
    client.close()

def getData(ac):
    client=sqlite3.connect('BankMng.db')
    c=client.cursor()
    c.execute("SELECT * FROM acno where _id = (?)", (ac,))
    data=c.fetchone()
    print('Name:\t',data[1],'\nPassword:\t',data[2],'\nAccount No.:\t',data[0],'\nBalance:\t',data[3],'\nDate:\t',data[4],'\nTime:\t',data[5])
    print('Data displayed Successfully!!')
    client.commit()
    client.close()
    
   
def create():
    name=input('Enter Name for new account:\t')
    password=input('Enter Password for new account:\t')
    acno=random.randrange(10000000,99999999)
    dd=datetime.datetime.now()
    date=dd.strftime("%d/%m/%Y")
    time=dd.strftime("%X")+" "+dd.strftime("%p")
    balance=0
    client=sqlite3.connect('BankMng.db')
    c=client.cursor()
    c.execute("INSERT INTO acno VALUES (?,?,?,?,?,?)", (acno,name,password,balance,date,time))
    print('Account created Successfully!!')
    client.commit()
    client.close()
    getData(str(acno))

