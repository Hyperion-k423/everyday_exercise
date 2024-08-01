import random
num = random.randint(1,10)
guess = int(input("第一次："))
if guess == num:
    print("猜对了")
else:
    if guess < num:
        print("小了")
    else:
        print("大了")
    guess = int(input("第二次："))
    if guess == num:
        print("猜对了")
    else:
        if guess < num:
            print("小了")
        else:
            print("大了")
    guess = int(input("最后一次："))
    if guess == num:
        print("猜对了")
    else:
        print(f"失败了，正确答案是：{num}")



i=1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"{sum}")
