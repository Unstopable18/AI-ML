print("1  Add user ")
print("2  Delete user ")
print("3  Modify the user ")
print("4  Query the user ")
print("5  exit ")

fname=input("Enter First name:\t")
mname=input("Enter Middle name:\t")
lname=input("Enter Last name:\t")

allEmp=list()
type = int(input(" Please select: "))
while type>=1 and type<=5:
  if type==1:
    id = input(" Please enter the user's id:")
    name = input(" Please enter the user's name: ")
    pw = input(" Please enter user password: ")
    allEmp.append([id,name,pw])
    print(" Added successfully! ")
  elif type==2:
    # Determine if the user is present ids There are 
    id = input(" Please enter the user's id:")
    for i in range (len(allEmp)):
        if id in allEmp[i]:
            allEmp.pop(i)
            print(" Deleted successfully! ")
        else:# No user prompt was found 
          continue
  elif type==3:
    # Determine if the user is present ids There are 
    id = input(" Please enter the user's id:")
    for i in range (len(allEmp)):
        if id in allEmp[i]:
            allEmp[i][1]= input(" Please enter the user's name :")
            allEmp[i][2]= input(" Please enter the user's password :")
            print(" Modified successfully! ")
        else:# No user prompt was found 
          continue
  elif type==4:
    # Determine if the user is present ids There are 
    id = input(" Please enter the user's id:")
    for i in range (len(allEmp)):
        if id in allEmp[i]:
          print(" The user's id:",allEmp[i][0])
          print(" The user name :",allEmp[i][1])
          print(" The user password :",allEmp[i][2])
          print(" Quried Successfully! ")
        else:# No user prompt was found 
          continue
  elif type==5:
    print(" Thank You! ")
    break
  print(allEmp)
  type = int(input(" Please select: "))
else:
  print(" Incorrect input! ")