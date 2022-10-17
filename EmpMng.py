print("".center(50,'*'))
print("1:Add")
print("2:Delete")
print("3:Update")
print("4:Data Fetch")
print("5:Exit")
print("".center(50,'-'))
allEmp=list()
type = int(input("Please select (1-5):\t"))
print("".center(50,'*'))
while type>=1 and type<=5:
  if type==1:
    empId = input("Please enter Employee Id:\t")
    name=input("Enter Full Name:\t")
    mob=input("Enter Mobile No.:\t")
    salary=input("Enter Salary:\t")
    allEmp.append([empId,name,mob,salary])
    print(" Added successfully! ")
  elif type==2:
    empId = input("Please enter Employee Id:\t")
    for i in range (len(allEmp)):
        if empId in allEmp[i]:
            allEmp.pop(i)
            print(" Deleted successfully! ")
        else: 
          continue
  elif type==3:
    empId = input("Please enter Employee Id:\t")
    for i in range (len(allEmp)):
        if empId in allEmp[i]:
            print("".center(50,'-'))
            print("1:Update Full Name")
            print("2:Update Mobile No.")
            print("3:Update Salary")
            print("4:Exit Update")
            print("".center(50,'-'))
            utype = int(input("Please select (1-4):\t"))
            print("".center(50,'-'))
            while utype>=1 and utype<=4:
              if utype==1:
                allEmp[i][1]=input("Enter Full Name:\t")
                print(" Modified successfully! ")
              elif utype==2:
                allEmp[i][2]=input("Enter Mobile No.:\t")
                print(" Modified successfully! ")
              elif utype==3:
                allEmp[i][3]=input("Enter Salary:\t")
                print(" Modified successfully! ")
              elif utype==4:
                print(" Update Exited ")
                break
              print("".center(50,'-'))
              print(allEmp)
              print("".center(50,'-'))
              utype = int(input("Please select Update type (1-4):\t"))
            else:
              print(" Invalid Input! ")
        else: 
          continue
  elif type==4:
    empId = input("Please enter Employee Id:\t")
    for i in range (len(allEmp)):
        if empId in allEmp[i]:
          print(" Employee empId:\t",allEmp[i][0])
          print(" Full Name:\t",allEmp[i][1])
          print(" Mobile No:\t",allEmp[i][2])
          print(" Salary:\t",allEmp[i][3])
          print(" Data Fetched Successfully! ")
        else: 
          continue
  elif type==5:
    print(" Thank You! ".center(50,'*'))
    break
  print("".center(50,'-'))
  print(allEmp)
  print("".center(50,'*'))
  type = int(input("Please select (1-5):\t"))
else:
  print(" Invalid Input! ")