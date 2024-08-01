i = 1
while i<= 9:
    j = 1
    while j <= i :
        print(f"{j}*{i}={j * i}\t", end='')
        j += 1
    print("\n")
    i +=1

name = "inheima is a brand of itcast"
i = 0
for x in name :
    if x == "a" :
        i += 1
print(f"{name}里有{i}个a")

i = 0
for x in range(1,100):
    if x%2==0 :
        i+=1
print(i)
