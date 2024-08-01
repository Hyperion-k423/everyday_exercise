#1
money=10000
for x in range(1,21):
    import random
    num=random.randint(1,10)
    if num<5:
            print(f"员工{x}，绩效分{num}，低于5，不发工资，下一位。")
    else:
        if money >= 1000:
            money-=1000
            print(f"向员工{x}发放工资1000元，账户余额还剩余{money}元")
        else:
            print("工资发完了，下月领取吧")
            break
#2
def pr():
    print("欢迎来到黑马程序员!\n请出示您的健康码以及72小时核酸证明!")
pr()#调用实例
#3
tem=float(input("欢迎来到黑马程序员!请出示您的健康码以及72小时核酸证明，并配合测量体温!\n请输入体温:"))
if tem <= 37.5:
    print("体温测量中，您的体温是:%.1f度，体温正常请进!"%tem)
else:
    print(f"体温测量中，您的体温是:%.1f度，需要隔离!"%tem)