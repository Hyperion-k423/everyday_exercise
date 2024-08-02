money = 500000
name = None
name = input("Enter your name: ")
def query(show_header):
    if show_header:
        print("-------查询-------")
    print(f"{name},您的余额为：{money}")
def saving(num):
    global money
    money += num
    print("-------存款-------")
    print(f"{name}，您成功存款{money}元")
    query(False)
def getting_money(num):
    global money
    money -= num
    print("-------取款-------")
    print(f"{name},您成功取款{money}元")
    query(False)
def main():
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("推出\t\t【输入4】")
while True:
    main()
    key_name = input("请输入您的选择 ")
    if key_name == "1":
        query(True)
        continue
    elif key_name == "2":
        num = int(input("您要存款多少元"))
        saving(num)
        continue
    elif key_name == "3":
        num = int(input("您要取款多少元"))
        getting_money(num)
        continue
    else:
        print("退出啦")
        break



