import csv

f1 = open('Q-2/file1.csv','r')
read = csv.DictReader(f1)

for row in read :
    roll_num = row["ROLL NO"]
    name = row['NAME']
    sub1 = int(row['SUB1'])
    sub2 = int(row['SUB2'])
    sub3 = int(row['SUB3'])
    total = sub1+sub2+sub3

dictionary={"ROLL NO":roll_num , "NAME":name , "SUB1":sub1,"SUB2":sub2,"SUB3":sub3, "TOTAL":total}
print(dictionary)

#OUTPUT:
# {'ROLL NO': '1', 'NAME': 'raj', 'SUB1': 82, 'SUB2': 75, 'SUB3': 91, 'TOTAL': 248}
