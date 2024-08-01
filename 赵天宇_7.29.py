# 7.29
练习1
import random
num = random.randint(1,10)
guess_num = int(input("输入你要猜的数字："))
if guess_num == num:
    print("猜对了")
else:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")

guess_num = int(input("输入你要猜的数字："))
if guess_num == num:
    print("猜对了")
else:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")

guess_num = int(input("输入你要猜的数字："))
if guess_num == num:
    print("猜对了")
else:
    print("猜错了，机会用完了")

# 练习二
i = 1
sum = 0
if i<=100:
    sum += i
    i += 1

print(f"1-100的和为{sum}")
