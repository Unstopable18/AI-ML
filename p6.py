def add(num,*snum):
    sum=0
    for i in snum:
        sum+=i
    print('First num is:\t',num,'\nSum of all numbers passed:\t',sum)

add(23,10,5,5)