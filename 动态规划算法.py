
p=[0,408,921,1329,11,998,1009,104,839,943,299,374,673,703,954,1657,425,950,1375,430,541,971,332,483,815,654,706,1360,956,992,1948]
w=[0,508,1021,1321,111,1098,1196,204,939,1107,399,474,719,803,1054,1781,525,1050,1362,530,641,903,432,583,894,754,806,1241,1056,1092,1545] 
c=10149
n=30





import datetime

starttime = datetime.datetime.now()


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
        if j<w[i]:
            f[i][j]=f[i-1][j]
        else:
            f[i][j]=max(f[i-1][j],f[i-1][j-w[i]]+p[i]);

file1=open("result.txt",'w')

x2="背包能装的最大价值是："+str(f[n][c])
file1.write(x2)
print("背包能装的最大价值是：",f[n][c])
j=c;

for i in range(n,0,-1):
    if f[i][j]>f[i-1][j]:
        x[i]=1
        j=j-w[i]
    else:
        x[i]=0
    print(x[i],end=' ')
x2="\n装入背包的物品是："+str(x)
file1.write(x2)
    


endtime = datetime.datetime.now()

x2='\n运行时间为：'+str(endtime - starttime)
print ('\n运行时间为：',(endtime - starttime))
file1.write(x2)
file1.close()

        

    
