f1 = open('6dirs/sample1.txt','r')
f2 = open('6dirs/sample2.txt','r')
f3 = open('6dirs/sample3.txt','a+')

data1 = f1.readlines()
data2 = f2.readlines()
len1= len(data1)
len2 = len(data2)
if len1>len2:
    dif = len1 -len2
    for i in range(0,len(data2)):
        f3.write(data1[i])
        f3.write(data2[i])
    for i in range(-1,dif,-1):
        f3.write(data1[i])

elif len1<len2:
    dif1 = len2 -len1
    for i in range(0,len(data1)):
        f3.write(data1[i])
        f3.write(data2[i])
    for i in range(-1,dif1,-1):
        f3.write(data2[i])

print("task done successfully")

#OUTPUT:
# task done successfully