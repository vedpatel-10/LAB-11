import os
f = open('Q-4/sub_dir1/sample1.txt.txt','r')
data = f.read()
os.makedirs('.\\dirs1\\dirs2')
os.chdir('.\\dirs1\\dirs2')
f1 = open('sample2.text','w+')
f1.write(data)

#OUTPUT:
# text from sample1.txt.txt is copied to recently
# created sub-directory sample2.txt

