import csv
data = [["name","place"],["abhishek",'mumbai'],["harsh",'pune']]

f1 = open('file1.csv',mode='w+',newline='',encoding='utf-8')
csv_obj =csv.writer(f1)
csv_obj.writerows(data)

print("task completed.")

#OUTPUT:
# task completed.