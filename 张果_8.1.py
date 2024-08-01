name=None
money=5000000
name=input("请输入用户名：")
def chaxun():
    print(f"{name}，您好，您的余额剩余:{money}")

def pb():
    print("--------主菜单--------")
    print(f"{name}，您好，欢迎来到黑马银行ATM。")
def zcd(name):
    print(f"请选择操作:\n查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")
    return int(input("请输入您的选择:"))

def cun(num1):
    global money
    money+=num1
    print(f"{name}，您好，您存款{num1}元成功")
    chaxun()

def qu(num2):
    global money
    money -= num2
    print(f"{name}，您好，您取款{num2}元成功")
    chaxun()

pb()
while 1:
    num=zcd(name)
    if num == 1:
        print("-------查询金额-------")
        chaxun()
    elif num==2:
        print("--------存款--------")
        num1=int(input("存款金额:"))
        cun(num1)
    elif num==3:
        print("--------取款--------")
        num2 = int(input("取款金额:"))
        qu(num2)
    elif num==4:
        break

print("操作结束，已退出")