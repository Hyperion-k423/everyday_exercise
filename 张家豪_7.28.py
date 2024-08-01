# 判断语句
# 布尔类型
bool_1 = True
print(f"bool_1 的内容是是{bool_1},结果是{type(bool_1)}")
# 比较运算符
num_1 = 10
num_2 = 10
print(f"num_1 == num_2的结果是{num_1 == num_2}")
print(f"num_1 >= num_2的结果是{num_1 >= num_2}")
name_1 = "man"
name_2 = "bin"
print(f"name_1 == name_2的结果是{name_1 == name_2}")
# if语句
"""
if 条件:
    （记得缩进四个空格）条件成立，接下来执行什么
"""
age = 20
if age >= 18:
    print("i am an adult")
print("how time flies")
# if - else 语句
# if - elif - else语句
height = int(input("请输入您的身高："))
vip_level = int(input("请输入您的级别："))
if height<=120:
    print("您可以免费游玩")
elif vip_level > 3:
    print("您可以免费游玩")
else:                            # else可以省略
    print("请补票")
# 下面是清新简洁版
if int(input("请输入您的身高")) < 120:
    print("您可以免费游玩")
elif (int(input("请输入您的级别"))) > 3:
    print("您可以免费游玩")
else :
    print("请补票")
# 7-28练习 成年人判断
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age = input("请输入您的年龄：")
if int(age)>=18:               # input()输入的都是字符串类型，输入数字后需要手动转换为整数类型
    print("您已成年，游玩需要补票10元")  #所以可以这样 age = int(input("请输入您的年龄："))
else :
    print("您未成年，可以免费游玩")
print("祝您游玩愉快")
# 7-28 我要买票吗
print("欢迎来到黑马动物园")
age = int(input("请输入您的身高(cm):"))
if age>= 120:
    print("您的身高超过120cm,游玩需要买票10元")
else:
    print("您的身高未超过120cm，可以免费游玩")
print("祝您游玩愉快")
# 7-28练习 猜猜心里数字
num = int(input("请输入第一次猜想的数字"))
if num ==5:
    print("恭喜你猜对了")
elif int(input("对不起，再猜一次")) == 5:    #elif后面只能跟一行内容吗？
    print("恭喜猜对了")
elif int(input("对不起，再踩最后一次")) == 5:
    print("恭喜猜对了")
else :
    print("很抱歉，机会用完了")
