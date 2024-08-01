#1
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print()
#2
name="itheimais abrand ofitcast"
#2.1
count=name.count("a")
print(f"共有{count}个a")
#2.2
count2=0
for x in name:
    if x=="a":
        count2+=1
print(f"共有{count2}个a")
#3
num=100
count3=0
for x in range(1,num):
    if x%2==0:
        count3+=1
print(f"1到{num}(不含{num}本身)范围内，有{count3}个偶数")
#4
for x in range(1,10):
    for y in range(1,x+1):
        print(f"{y}*{x}={y*x}\t",end="")
    print()