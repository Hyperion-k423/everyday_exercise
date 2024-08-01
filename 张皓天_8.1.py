money = 5000000
name = input()
def balance() :
    print("余额查询")
    print(f"{name}，您好，您的余额剩余：{money}元")
def deposit(cash) :
    print("存款")
    print(f"{name},您好，您存款{cash}元成功")
    global money
    money = money + cash
    print(f"{name},您好，您的余额剩余：{money}元  ")
def withdrawal(cash) :
    print("取款")
    print(f"{name},您好，您取款{cash}元成功")
    global money
    money = money - cash
    print(f"{name},您好，您的余额剩余：{money}元")
def menu() :
    print("主菜单")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款     \t【输入2】")
    print("取款     \t【输入3】")
    print("退出     \t【输入4】")
    return int(input("请输入您的选择:"))
while True:
    key_word = menu()
    if key_word == 1 :
        balance()
    elif key_word == 2 :
        cash = int(input("您想存入多少钱："))
        deposit(cash)
    elif key_word == 3 :
        cash = int(input("您想取出多少钱："))
        withdrawal(cash)
    elif key_word == 4 :
        exit()