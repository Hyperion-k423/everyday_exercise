#1
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age=input("请输入你的年龄:")
if int(age) >= 18:
    print("您已成年，游玩需要补票10元。")
print("祝您游玩愉快。")
#2
print("欢迎来到黑马动物园。")
high=int(input("请输入你的身高(cm):"))
if high>120:
    print("您的身高超出120cm，游玩需要够票10元")
else:
    print("您的身高未超出120cm，可以免费游玩")
print("祝您游玩愉快。")

#3
num=10
NUM=int(input("请输入第一次猜想的数字:"))
if NUM==num:
    print("猜对了")
else:
    if int(input("不对，再猜一次:"))==num:
        print("猜对了")
    else:
        if int(input("不对，再猜最后一次:")) == num:
            print("猜对了")
        else:
            print("Sorry，全部猜错啦，我想的是:10")