# 练习1  \t对齐  end=''不换行 print空内容=换行
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')
        j += 1
    i += 1
    print()

# 练习2
count = 0
name = "itheima is a brand of itcast"
for x in name:
    if x == "a":
        count += 1

print(f"被统计的字符串有{count}个a")

# 练习3
# range(num)获取一个从0开始到num结束的数字序列，不含num本身
# range(num1,num2)获取一个从num1开始，到num2结束的数字序列，不含num2本身
# range(num1,num2,step)获得一个从num1开始到num2结束的数字序列，不含num2，数字之间的步长，以step为准（默认为1）
count = 0
num = int(input())
for x in range(1,num):
    if x % 2 == 0:
        count += 1
print(f"1到{num}(不含{num}本身)范围内有{count}个偶数")

# 练习4
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t", end='')
    print()



