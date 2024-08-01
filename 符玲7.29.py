#7.29-1
i=1
sum=0
while i<=100:
    sum=sum+i
    i+=1
print(f"1-100的和：{sum}")
#7.29-2
import random
num=random.randint(1,10)
gess_num=int(input("输入你要猜测的数字："))
if gess_num==num:
    print("恭喜你第一次就猜中了")
else:
    if gess_num>num:
        print("你猜测的数字大了")
    else :
        print("你猜测的数字小了")
        gess_num=int(input("再次输入你想要的数字"))
    if  gess_num==num:
        print("恭喜你第二次猜中了")
    else :
        if gess_num>num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")
        gess_num=int(input("第三次输入你要猜测的数字："))
        if gess_num==num:
            print("第三次猜中了")
        else:
            print("三次机会用完，没有猜中。")










