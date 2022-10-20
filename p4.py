def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)


print("1:Add")
print("2:Subtract")
print("3:Mulitply")
print("4:Divide")
print("5:Exit")
print("".center(50,'-'))
a = int(input("Enter First num:\t"))
b = int(input("Enter Second num:\t"))
type = int(input("Please select (1-5):\t"))
print("".center(50,'*'))
while type>=1 and type<=5:
    if type==1:
        print(a,' ','+',' ',b,' ','=', (a+b))
        print('Function call:', add(a,b))

    elif type==2:
        print(a,' ','-',' ',b,' ','=', (a-b))
        print('Function call:', sub(a,b))

    elif type==3:
        print(a,' ','*',' ',b,' ','=', (a*b))
        print('Function call:', mul(a,b))

    elif type==4:
        print(a,' ','/',' ',b,' ','=', (a/b))
        print('Function call:', div(a,b))

    elif type==5:
        print(" Thank You! ".center(50,'*'))
        break

    print("".center(50,'*'))
    type = int(input("Please select (1-5):\t"))
else:
  print(" Invalid Input! ")