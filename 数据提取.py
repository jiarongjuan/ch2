
print('\n','*'*8+'读入数据文件的有效DKP数据'+'*'*8,'\n')
x=input("输入你要提取数据的文件名称：  ")
with open(x,'r') as f:
  message=f.readlines()
a='The profit of items are:'
b='The weight of items are:'
y1=input("输入价值数据文件名:")
file1=open(y1,'w')
y2=input("输入重量数据文件名:")
file2=open(y2,'w')
for i in range(len(message)):
    if message[i][:24]==a:
        file1.write(message[i+1])
    if message[i][:24]==b:
        file2.write(message[i+1])
file1.close()
file2.close()
print("\n数据已经提出，保存在你的文件中")
