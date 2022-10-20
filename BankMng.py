from BankMngFunction import *

print("1:Create Account")
print("2:Credit")
print("3:Debit")
print("4:Balance Check")
print("5:View Data")
print("6:Exit")
print("".center(50,'-'))
type = int(input("Please select (1-6):\t"))
print("".center(50,'-'))
while type>=1 and type<=6:
    if type==1:
        create()
    elif type==2:
        credit()
    elif type==3:
        debit()
    elif type==4:
        balance()
    elif type==5:
        ac=input('Enter Account No.:\t')
        getData(ac)
    elif type==6:
        print(" Thank You for banking with us! ".center(50,'*'))
        break
    print("".center(50,'*'))
    type = int(input("Please select (1-5):\t"))
else:
  print(" Invalid Input! ")