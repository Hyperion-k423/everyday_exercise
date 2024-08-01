print(f"欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入你的年龄:"))
if age >= 18:
    print(f"您已成年，游玩需要补票10元。")
print(f"祝您游玩愉快。")
print(f"欢迎来到黑马动物园。")
gao = int(input("请输入你的身高(cm):"))
if gao > 120:
    print(f"您的身高超出120cm，游玩需要够票10元")
else:
    print(f"您的身高未超出120cm，可以免费游玩。")
print(f"祝您游玩愉快。")

stand = 6
num = int(input("请输入第一次猜想的数字:"))
if num != stand:
    print("不对，再猜一次:")
    num1 = int(input())
    if num1 != stand:
        print("不对，再猜一次：")
        num2 = int(input())
        if num2 != stand:
            print(f"Sorry，全部猜错啦，我想的是:6")
        else:
            print(f"对啦")
    else:
        print(f"对啦")
else:
    print(f"对啦")
