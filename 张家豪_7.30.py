# print()语句不换行
print("hello,",end='')
print("world",end='')
# 制表符\t
print("\nhello\tworld")
print("best\tyou")
# for 循环（对内容进行逐个处理——遍历循环；与while循环不同，没有循环条件 ，理论上构建不成无限循环）
name = "man"
for x in name :    #将name变量中的内容逐个取出赋予到临时变量x中
    print(x)
# range()语句
# rang()语法1
for x in range(10) :
    print(x,end='')
print() #这一行是为了使上面的模块和下面的模块分开
# range()语法2
for x in range(5,10) :
    print(x,end='')
print()
#range()语法3
for x in range(8,16,2) :
    print(x,end='')
print()
#7-30九九乘法表（while版）
i = 1
while i<= 9:
    j = 1    # j的控制在第一个while里面，使其能从1开始递增到i
    while j <= i :
        print(f"{j}*{i}={j * i}\t", end='')
        j += 1
    print("\n")     # 每一行输出完后进行换行，但这样每一行会相隔一行，所以可以直接用print()进行无缝换行
    i +=1
# 九九乘法表（for版）
i = 1
for i in range(1,10) :
    for j in range(1,i+1) :
        print(f"{j}*{i}={j * i}\t", end='')
    print()
#7-30数一数有几个a
name = "inheima is a brand of itcast"
i = 0
for x in name :
    if x == "a" :
        i += 1
print(f"{name}里有{i}个a")
#7-30 有几个偶数
i = 0
for x in range(1,100):
    if x%2==0 :
        i+=1
print(i)
