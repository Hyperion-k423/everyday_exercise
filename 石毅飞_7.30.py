i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}",end = " 0  ")
        j += 1
    i+=1
    print(" ")



name ="itheima is a brand of itcast"
count = 0
for i in name:
    if i=="a":
        count=count+1
print(count)

num = 50
count = 0
for i in range(1,num):
    if i % 2 == 0:
        count=count+1
print(count)


for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end = " ")
    print(" ")
