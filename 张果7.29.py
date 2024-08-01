#1
import random
num = random.randint(1,10)
NUM=int(input("请输入第一次猜想的数字:"))
if NUM==num:
    print("猜对了")
else:
    if(NUM<num):
        print("小了")
    else:
        print("大了")
    NUM=int(input("再猜一次:"))
    if NUM==num:
        print("猜对了")
    else:
        if (NUM < num):
            print("小了")
        else:
            print("大了")
        NUM = int(input("再猜一次:"))
        if NUM == num:
            print("猜对了")
        else:
            print(f"Sorry，全部猜错啦，我想的是:{num}")
#2
sum=0
i=0
while 1:
    i+=1
    sum+=i
    if i==100:
        break
print(f"从1到100的累加和为：{sum}")