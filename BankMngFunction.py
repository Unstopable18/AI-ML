import datetime
import random
import json
    
def credit():
    f = open('sample.json',)        
    data = json.load(f)
    try:
        ac=int(input('Enter Account No.:\t'))
        try:
            for i in data['bank_account']:
                for j in i:
                    if ac in j:
                        amt=float(input('Enter amount to be credited:\t'))
                        i[ac]["balance"]=float(i[ac]["balance"])+amt
                        w_file=open('sample.json','w')
                        json.dump(data,w_file,indent = 4)
                        w_file.close()
                        getData(ac)
                        return print('Balance:\t',i[ac]["balance"])
                    else:
                        continue
            return print('Account not found!!!')
        except Exception as msg:
            print(msg.__class__.__name__,' Occured!!!!')
    except ValueError:
        print('Please enter Numeric value only!!!')
    

def debit():
    f = open('sample.json',)        
    data = json.load(f)
    try:
        ac=int(input('Enter Account No.:\t'))
        try:
            for i in data['bank_account']:
                for j in i:
                    if ac in j:
                        amt=float(input('Enter amount to be debited:\t'))
                        if(i[ac]["balance"]>=amt):
                            i[ac]["balance"]=float(i[ac]["balance"])-amt
                            w_file=open('sample.json','w')
                            json.dump(data,w_file,indent = 4)
                            w_file.close()
                            getData(ac)
                            return print('Balance:\t',i[ac]["balance"])
                        else:
                            print('Insufficient Balance!!!')
                    else:
                        continue
            return print('Account not found!!!')
        except Exception as msg:
            print(msg.__class__.__name__,' Occured!!!!')
    except ValueError:
        print('Please enter Numeric value only!!!')
    
def balance():
    f = open('sample.json',)        
    data = json.load(f)
    try:
        ac=int(input('Enter Account No.:\t'))
        try:
            for i in data['bank_account']:
                for j in i:
                    if str(ac) in j:
                        return print('Balance:\t',i[str(ac)]["balance"])
                    else:
                        continue
            return print('Account not found!!!')
        except Exception as msg:
            print(msg.__class__.__name__,' Occured!!!!')
    except ValueError:
        print('Please enter Numeric value only!!!')

    

def getData(ac):
    f = open('sample.py',)        
    data = json.load(f)
    try:
        for i in data['bannk_account']:
            for j in i:
                if ac in j:
                    return print('Name:\t',i[ac]["name"],'\nPassword:\t',i[ac]["password"],'\nAccount No.:\t',ac,'\nBalance:\t',i[ac]["balance"],'\nDate:\t',i[ac]["date"],'\nTime:\t',i[ac]["time"])
                else:
                    continue
        return print('Account not found!!!')
    except Exception as msg:
        print(msg.__class__.__name__,' Occured!!!!')

def write_json(new_data, filename='sample.py'):
	with open(filename,'r+') as file:
		file_data = json.load(file)
		file_data["bank_account"].append(new_data)
		file.seek(0)
		json.dump(file_data, file, indent = 4)
        
def create():
    name=input('Enter Name for new account:\t')
    password=input('Enter Password for new account:\t')
    acno=random.randrange(10000000,99999999)
    dd=datetime.datetime.now()
    date=dd.strftime("%d/%m/%Y")
    time=dd.strftime("%X")+" "+dd.strftime("%p")
    balance=0
    data = {acno:{
            "name":name,
            "password": password,
            "balance":balance,
            "date":date,
            "time":time
	}}
    write_json(data)
    print('Account created Successfully!!')
    getData(str(acno))
