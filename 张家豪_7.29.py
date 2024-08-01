# 判断语句的嵌套
if int(input("你的身高是多少：")) > 120:
    print("你的身高超出限制，不能免费")
    print("如果你的vip级别>3，也可以免费")
    if int(input("请输入您的vip级别：")) >3 :
        print("您可以免费游玩")
    else :
        print("sorry,you can't")
else :
    print("欢迎免费游玩")
# 领取礼物
age=int(input("请输入你的年龄："))
if age>=18:
    print("您已成年")
    if age <=30:
        print("您的年龄达标了")
        if int(input("请输入您的入职年龄："))>=3 :
            print("您可以领取礼物")
        elif  int(input("请输入您的级别："))>=3:
            print("您可以领取礼物")
        else :
            print("sorry,您的入职时间和级别都不达标")
    else :
        print("sorry,您的年龄未达标")
else :
    print("sorry,您未成年") #原来屎山代码就是这么来的，多来几个嵌套还不把人绕晕了
# 循环语句
# 沸羊羊程序
i = 0
while i<100 :     # 与c不同，不能写while i= 0 < 100
    print("xx i love you")
    i+=1
# 7-29 求1-100的和
i = 1
sum = 0
while i<=100 :
    sum = sum + i
    i+=1
print("1到100的和是%d" %sum)
#while 的嵌套
i = 1
while i<=100:        # 内层嵌套
    print("今天是第%d天，准备表白" %i)

    j = 1
    while j<= 10:
        print("送给小美第%d枝玫瑰花" %j)
        j +=1
    print("小美，我喜欢你")
    i += 1
print(f"坚持到第{i-1}天表白成功")
# 7-29 猜数字
import random
num = random.randint(1,10)
guess_num = int(input("请输入你猜测的数字："))
if guess_num == num :
    print("恭喜你猜中了")
else :
    if guess_num > num:
        print("猜的数字大了")
        guess_num = int(input("请再次输入你猜测的数字："))
        if guess_num == num:
            print("恭喜你猜中了")
        else:
            if guess_num > num:
                print("猜的数字大了")
                guess_num = int(input("请第三次输入你猜测的数字："))
                if guess_num == num:
                    print("恭喜你猜中了")
                else:
                    print("sorry.游戏结束了")
            else:
                print("猜的数字小了")
                guess_num = int(input("请第三次输入你猜测的数字："))
                if guess_num == num:
                    print("恭喜你猜中了")
                else:
                    print("sorry.游戏结束了")
    else:
        print("猜的数字小了")
        guess_num = int(input("请再次输入你猜测的数字："))
        if guess_num == num:
            print("恭喜你猜中了")
        else:
            if guess_num > num:
                print("猜的数字大了")
                guess_num = int(input("请第三次输入你猜测的数字："))
                if guess_num == num:
                    print("恭喜你猜中了")
                else:
                    print("sorry.游戏结束了")
            else :
                print("猜的数字小了")
                guess_num = int(input("请第三次输入你猜测的数字："))
                if guess_num == num:
                    print("恭喜你猜中了")
                else:
                    print("sorry.游戏结束了")
# 用while循环猜数字
import random
num = random.randint(1,10)
flag = True # 引入一个终止循环的条件
count = 0
while flag:
    guess_num = int(input("请输入您猜的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else :
        if guess_num > num :
            print("猜的数大了")
        else:
            print("猜的数小了")
print("您一共猜了%d次" %count)



