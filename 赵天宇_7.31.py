# 练习1
money = 10000
for i in range(1,20):
    import random
    score = random.randint(1,10)
    if score < 5:
        print(f"员工{i}绩效分低，不发工资")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}，满足条件发放工资1000元，公司账户余额{money}")
    else:
        print(f"余额不足，当前余额{money}元")
        break

# 练习2
def huanying():
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码以及72小时核酸证明！")

huanying()

# 练习3
def check(num):
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码以及72小时核酸证明！")
    if num <= 37.5:
        print(f"您的体温为{num}度，体温正常，请进")
    else:
        print(f"您的体温为{num}度，需要隔离")

import random
num = random.randint(35,42)
check(num)
