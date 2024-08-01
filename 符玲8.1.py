
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















































