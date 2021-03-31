
print('\n','*'*8+'DKP问题'+'*'*8,'\n')



print('\n','*'*8+'读入有效数据'+'*'*8,'\n')
x1=input("你要提取哪个文件的数据的：  ")
with open(x1,'r') as f:
  message=f.readlines()


a='The profit of items are:'
b='The weight of items are:'
d='the cubage of knapsack is'

y1=input("输入价值数据文件名:")
file1=open(y1,'w')
y2=input("输入重量数据文件名:")
file2=open(y2,'w')
l1=[]

for i in range(len(message)):
    if message[i][:24]==a:
        file1.write(message[i+1])
        e=message[i-1]
        e1="the cubage of knapsack is"
        e2=e.index(e1)
        l1.append(int(e[e2+len(e1)+1:-2]))
    if message[i][:24]==b:
        file2.write(message[i+1])

file1.close()
file2.close()


print("数据已经提出，保存在你定义的文件中\n")

with open(y2,'r') as file1:
    message1=file1.readlines()
with open(y1,'r') as file2:
    message2=file2.readlines()


x2=int(input("你要选择该文件的第几组数据（0—9）"))
c=l1[x2]
list2=[]
list3=[]

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


print("背包容量为：",c,"\n物品重量为：",list2[x2],"\n物品价值为：",list3[x2])


print('\n','*'*8,'这组数据的散点图展示','*'*8,'\n')



print('\n','*'*8,'按照第三项集的展示如下','*'*8,'\n')

list4=[]
for i in range(2,len(list2[x2])+1):
    if i%3==0:
        list4.append(round(list3[x2][i-1]/list2[x2][i-1],3))
print("这组数据的性价比为:")
print(list4)
list4.sort(reverse=True)
print("\n非递增的排序结果如下所示:")
print(list4)


print('\n','*'*8,'动态规划算法解决','*'*8,'\n')

n=len(list2[x2])

import datetime

starttime = datetime.datetime.now()

list2[x2].insert(0,0)
list3[x2].insert(0,0)

x=[]
f=[]
for i in range(n+1):
    x.append(0)
for i in range(n+1):
    f.append([])

for i in range(n+1):
    for j in range(c+1):
        f[i].append(0)
    
for i in range(1,n+1):
    for j in range(1,c+1):
        if j<list2[x2][i]:
            f[i][j]=f[i-1][j]
        else:
            f[i][j]=max(f[i-1][j],f[i-1][j-list2[x2][i]]+list3[x2][i]);

file3=open("result.txt",'w')
x3="背包能装的最大价值是："+str(f[n][c])
file3.write(x3)

j=c
for i in range(n,0,-1):
    if f[i][j]>f[i-1][j]:
        x[i]=1
        j=j-list2[x2][i]
    else:
        x[i]=0
x3="\n装入背包的物品是："+str(x)
file3.write(x3)
endtime = datetime.datetime.now()
x3='\n运行时间为：'+str(endtime - starttime)
file3.write(x3)
file3.close()
print("结果已经保存在result.txt文件中")
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(list2[x2],list3[x2])
plt.show()


#idkp1-10.txt






