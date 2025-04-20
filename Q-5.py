f1 = open('5dirs/f1.txt','r')
data = f1.readlines()
f2 = open('5dirs/f2.txt','a+')

for i in data:
    temp = i.upper()
    f2.write(temp)

print("task done successfully")

#OUTPUT:
# task done successfully
