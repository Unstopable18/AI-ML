import datetime
import random
import pymongo

client=pymongo.MongoClient('mongodb+srv://vaishnavi:8806812990@cluster0.acsdz4a.mongodb.net/test')
db=client['BankMng']
collection=db['bankAc']

def credit():
    try:
        ac=int(input('Enter Account No.:\t'))
        try:
            if(collection.find_one({"_id":ac},{"balance"})):
                amt=float(input('Enter amount to be credited:\t'))
                view=collection.find_one({"_id":ac},{"balance"})
                balance=view['balance']
                balance=balance+amt
                collection.update_one({"_id":ac},{'$set':{'balance':balance}})
                change=collection.find_one({"_id":ac},{"balance"})
                print('Balance:', change['balance'])
            else:
                print('Account not found!!!!!')
        except Exception as msg:
            print(msg.__class__.__name__,' Occured!!!!')
    except ValueError:
        print('Please enter Numeric value only!!!')
                        
    

def debit():
    try:
        ac=int(input('Enter Account No.:\t'))
        try:
            if(collection.find_one({"_id":ac},{"balance"})):
                amt=float(input('Enter amount to be debited:\t'))
                view=collection.find_one({"_id":ac},{"balance"})
                balance=view['balance']
                if(balance>=amt):
                    balance=balance-amt
                    collection.update_one({"_id":ac},{'$set':{'balance':balance}})
                    change=collection.find_one({"_id":ac},{"balance"})
                    print('Balance:', change['balance'])
                else:
                    print('Insufficient Balance!!!')
            else:
                print('Account not found!!!!!')
        except Exception as msg:
            print(msg.__class__.__name__,' Occured!!!!')
    except ValueError:
        print('Please enter Numeric value only!!!')
    
def balance():
    try:
        ac=int(input('Enter Account No.:\t'))
        try:
            if(collection.find_one({"_id":ac},{"balance"})):
                view=collection.find_one({"_id":ac},{"balance"})
                print('Balance:', view['balance'])
            else:
                print('Account not found!!!!!')
        except Exception as msg:
            print(msg.__class__.__name__,' Occured!!!!')
    except ValueError:
        print('Please enter Numeric value only!!!')

    

def getData(ac):
    view=collection.find_one({"_id":ac})
    return print('Name:\t',view["name"],'\nPassword:\t',view["password"],'\nAccount No.:\t',ac,'\nBalance:\t',view["balance"],'\nDate:\t',view["date"],'\nTime:\t',view["time"])
   
def create():
    name=input('Enter Name for new account:\t')
    password=input('Enter Password for new account:\t')
    acno=random.randrange(10000000,99999999)
    dd=datetime.datetime.now()
    date=dd.strftime("%d/%m/%Y")
    time=dd.strftime("%X")+" "+dd.strftime("%p")
    balance=0
    dictionary = {"_id":acno,
            "name":name,
            "password": password,
            "balance":balance,
            "date":date,
            "time":time
	}
    
    collection.insert_one(dictionary)
    print('Account created Successfully!!')
    getData(str(acno))
