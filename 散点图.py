print('\n','*'*8,'数据散点图','*'*8,'\n')
import numpy as np
import matplotlib.pyplot as plt


txt2=input("纵轴的价值文件名：")
txt1=input("横轴的重量文件名：")

x2=int(input("你要选择哪个项集（0—9）"))



with open(txt1,'r') as file1:
    message1=file1.readlines()
with open(txt2,'r') as file2:
    message2=file2.readlines()
list2=[]#存放重量
list3=[]#存放价值
for i in message1:
    str1=i[:-2].split(',')
    list1=[]
    for j in str1:
        list1.append(int(j))
    list2.append(list1)
for i in message2:
    str1=i[:-2].split(',')
    list1=[]
    for j in str1:
        list1.append(int(j))
    list3.append(list1)
x=list2[x2]
y=list3[x2]
plt.scatter(x,y)
plt.show()


'''

for i in range(len(list2)):
         x=list2[i]
         y=list3[i]
         plt.scatter(x,y)
         plt.show()
'''





         


    
    
