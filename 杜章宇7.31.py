sum = 10000
for i in range(1,21):
    import random
    num = random.randint(1,10)
    print(f"员工{i},绩效分{num},", end='')
    if num < 5:
        print("不发工资，下一位")
    else:
        sum -= 1000
        print(f"发放工资1000元，账户余额为{sum}")
    if sum == 0:
        break
print("工资发完了")


def said():
    print("欢迎来到王者荣耀！\n请出示充值记录")
said()



def COVID_19(x):
    if x <= 37.5:
        print(f"您的体温是{x}度，正常请进")
    else:
        print(f"您的体温是{x}度，需要隔离")

y = int(input())
COVID_19(y)
