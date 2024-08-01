# 7.28
# 练习1
print("欢迎来到黑马儿童游乐园，儿童免费，成人收费。")
age = int(input("请输入你的年龄:"))
if age >= 18:
    print("您已成年，游玩需要补票10元")
print("祝您游玩愉快")

# 练习2
height = int(input("请输入你的身高（cm）："))
if height > 120:
    print("您的身高超出120cm，需要买票，10元")
else:
    print("您的身高未超出120cm，可以免费游玩")
print("祝您游玩愉快")

# 练习3
num = 5
if int(input("请猜一个数字")) == num:
    print("恭喜第一次就猜对了")
elif int(input("猜错了，请再猜一次")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
else:
    print("sorry，猜错了")

