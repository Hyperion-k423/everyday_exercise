money=10000
for i in range(1,21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"绩效不足5，不发工资，下一位")
        continue

    if money >=1000:
            money -= 1000
            print(f"绩效达标，工资剩余{money}元")
    else:
        print("余额不足，下月再来")
        break

def my_s():
    print("欢迎来到黑马程序员")
    print("请出事您的健康码以及72小时核酸证明")
my_s()

def cheek(b):
    print("欢迎来到黑马程序员,请出事您的健康码以及72小时核酸证明,并配合测量体温")
    if b<= 37.5:
        print(f"体温测量中，您的体温是：{b},体温正常请进")
    else:
        print(f"体温测量中，您的体温是：{b},需要隔离")
cheek(37.6)

