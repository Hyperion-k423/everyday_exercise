import random
num = random.randint(1, 10)
num_1=int(input("请输入您第一次猜的数字"))
if num_1==num:
    print("恭喜您 猜对了")
else:
    if num_1>num:
        print("过大")
    elif num_1<num:
        print("过小")
    num_2=int(input("请输入您第二次猜的数字"))
    if num_2==num:
        print("恭喜您 猜对了")
    else:
        if num_2> num:
            print("过大")
        elif num_2 < num:
            print("过小")
        num_3= int(input("请输入您最后一次猜的数字"))
        if num_3==num:
            print("恭喜您 猜对了")
        else:
            if num_3 > num:
                    print("过大")
            elif num_3< num:
                    print("过小")
            print("您没有猜对")



sum = 0
i = 1
while i <=100:
    sum = sum + i
    i = i+1
print(f"1到100的累计和为：{sum}")
