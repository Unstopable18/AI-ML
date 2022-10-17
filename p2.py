#To find the number divisible by 7 and multiple of 5
"""num=5
while num<100:
    if num%7==0:
        print(num)
        break
    else:
        num+=5"""
grocery=['Oil','Sugar','Daal','rice','wheat','spices','washing powder','tea','matchbox','poha','biscuits']
print(grocery)
grocery.append('wicks')
print(grocery)
grocery.insert(0,'coriander')
print(grocery)
grocery.insert(0,['milk','butter'])
print(grocery)
#grocery.extend(['milk','butter'])
print(grocery)
n=len(grocery)

for i in range (n):
    print(grocery[i])
    i+=1
    
grocery.remove('biscuits')
print(grocery)
grocery[0].remove('butter')
print(grocery)
