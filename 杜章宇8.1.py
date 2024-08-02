num = 50000
def ask():
    print(f"您的余额剩余：{num}元")
def cun():
    new = int(input("您存款的金额："))
    global num
    num += new
    print(f"您当前余额为：{num}元")
def qu():
    re = int(input("您取款的金额："))
    global num
    num -= re
    print(f"您当前余额为：{num}元")
def main():
    print("周杰轮，您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额 [输入1]\n存款 \t[输入2]\n取款 \t[输入3]\n退出 \t[输入4]\t")

while True:
    main()
    use = int(input())
    if use == 1:
        ask()
        continue
    elif use == 2:
        cun()
        continue
    elif use == 3:
        qu()
        continue
    else:
        print("已退出")
        break
