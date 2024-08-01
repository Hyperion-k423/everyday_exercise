#7.30-1
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')#end=''保证不换行，\t表示每列对齐
        j=j+1
    i=i+1
    print()#输出一个换行
#7.30-2
count=0
name="itheima is a brand of itcast"
for x in name:#在name中依次取出字母赋值给x
    if x=="a":
        count+=1
print(f"一共有{count}个a")
#7.30-3
count=0
for i in range(1,100):#range（num1,num2)数列从num到num2-1
    if i%2==0:
        count+=1
print(f"1到100（不含100本身）范围内，有{count}个偶数")
#7.30-4
i=1
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
        j=j+1
    print()
























