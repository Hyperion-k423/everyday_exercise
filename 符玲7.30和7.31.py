
#7.31-1
x=10000
for i in range(1,21):
    import random
    num=random.randint(1,10)
    if num<5:
        print(f"员工{i},绩效分{num},低于5，不发工资，下一位")
        continue
    if x>=1000:
        x-=1000
        print(f"员工{i},满足条件发放工资1000元，公司账户余额：{x}")
    else:
        print(f"余额不足，当前余额：{x}元，不足以发工资，不发了，下个月再来")
        break
"""
    else :
        x=x-1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{x}元")
    if x==0:
        print("工资发完了，下个月领取吧")
        break
"""
#7.31-2
def shuoming():#定义函数
    print("欢迎来到黑马程序员！\n请出示您的健康码以及72小时核酸证明！")
shuoming()
#7.31-3
def add(a):
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if a>37.3:
        print(f"体温测量中，您的体温是{a}度，需要隔离！")
    else:
        print(f"体温测量中，您的体温是：{a}度，体温正常，请进!")
add(37.5)
#8.1-1
money=5000000
name=input("请输入您的姓名：")
def zhucaidan():
    print("----------菜单----------")
    print(f"{name}，您好，欢迎来到黑马银行  ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
def yu_e(show_header):#传入参数参数为真则打印
        if show_header:
            print("----------查询余额----------")
        print(f"{name},您好，您的余额剩余：{money}元")
def cunkuan(x):
    global money
    money=x+money
    print("----------存款----------")
    print(f"{name}您好，您存款{x}元成功\t{name},您好，您的余额剩余{money}元")
    yu_e(False)
def qukuan(y):
        global money
        money=money-y
        print("----------取款----------")
        print(f"{name},您取款{y}元成功")
        yu_e(False)
while True:
    num=zhucaidan()
    if num=='1':
        yu_e(True)
        continue
    elif num=='2':
        x=int(input("您想要存入多少钱？请输入："))
        cunkuan(x)
        continue
    elif num=='3':
        y=int(input("您想取出多少钱？请输入："))
        qukuan(y)
        continue
    else:
        print("程序退出")
        break















































