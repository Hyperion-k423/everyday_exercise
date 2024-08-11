age = [21, 25, 21, 23, 22, 20]
num = age
age.append(31)
age.extend([29, 33, 30])
age.pop(0)
age.pop(-1)
age.index(31)
print(f"{age}")


old_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_test = []
xin_test = []
ou = 0
while ou < len(old_test):
    element = old_test[ou]
    if element % 2 == 0:
        new_test.append(element)
    ou += 1
print(f"偶数为:{new_test}\t", end='')
print()
for ou in old_test:
    if ou % 2 == 0:
        xin_test.append(ou)
print(f"偶数为:{new_test}\t", end='')
print()

genshin = ('周杰伦', 11, ['football', 'music'])
age = genshin.index(11)
name = genshin[0]
del genshin[2][0]
genshin[2][0] = "coding"
print(genshin)


itest = "itheima itcast boxuegu"
count = itest.count("it")
new_test = itest.replace(" ", "|")
new_itest = new_test.split("|")
print(f"{new_itest}\t一共{count}个it")
