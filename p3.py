"""square=list()
for i in range (1,11):
    square.append(i*i)
print(square)"""

"""even=list()
for i in range (0,20):
    if i%2==0:
        even.append(i)
    else:
        continue
print(even) 
 
eeven=[i for i in range (0,20) if i%2==0]
#first part: final output 
#second part: iteration
#third part: condition
print(eeven)"""


maild=['vdeshmukh@cemtrexlabs.com','dkalaskar@cemtrexlabs.com','gmule@cemtrexlabs.com']
mail=list()
index=list()
for i in range (len(maild)):
    #index=maild[i].index('@')
    #mail.append(maild[i][0:index])
    index=maild[i].split('@')
    mail.append(index[0])
print('Traditional Method:\t', mail)

#mmail=[maild[i][0:(maild[i].index('@'))] for i in range (len(maild))]
mmail=[(maild[i].split('@'))[0] for i in range (len(maild))]
print('List Comprehension:\t', mmail)

