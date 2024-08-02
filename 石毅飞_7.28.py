age = int(input("请输入您的年龄: "))
if int(age) >=18:
    print("您已成年，游玩需要补票10元")
print("祝您游玩愉快")


height = int(input("请输入您的身高（cm）:"))
if height>120:
    print("您的身高超出120cm，游玩需要购票10元")
else:
    print ("您的身高未超出120cm，可以免费游玩")
print("祝您游玩开心")



num = 10
if int(input("请输入第一次猜想的数字："))==10:
    print("恭喜您猜对啦")
elif int(input("不对，再猜一次："))==10:
    print("恭喜您猜对啦")
elif int(input("不对，再猜最一次："))==10:
    print("恭喜您猜对啦")
else:
    print("Sorry，全部猜错啦，我想的是：",num)