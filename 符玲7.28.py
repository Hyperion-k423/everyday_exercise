#7.28-1
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age=input("请输入你的年龄：")#input输入都是字符串
age=int(age)#int变成整型
if age>=18:
    print("您已成年，游玩需要补票10元。")
print("祝您玩得愉快。")
#7.28-2
print("欢迎来到黑马动物园")
length=int(input("请输入你的身高（cm):"))
if length>120:
    print("您的身高超出120cm,游玩需要够票10元。")
else:
    print("您的身高未超出120cm,可以免费游玩。")
print("祝您玩的愉快。")
#7.28-3
shuzi=10
shuzi=int(input("请输入第一次猜想的数字："))
if shuzi==10:
    print("恭喜你第一次猜对了！")
elif int(input("猜错了，再猜一次："))==shuzi:
    print("猜对了")
elif int(input("猜错了，再猜一次："))==shuzi:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry,全部猜错啦，我想的是：10")
