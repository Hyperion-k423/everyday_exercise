mylist = [21,25,21,23,22,20]
mylist.append(31)
mylist.extend([29,33,30])
num1=mylist[0]
print(f"取出第一个元素{num1}")
num2=mylist[-1]
print(f"取出第二个元素{num2}")
index=mylist.index(31)
print(f"31的下标为{index}")
print(mylist)

my_str = "itheima itcas boxuegu"
count=my_str.count("it")
print(count)
new_str=my_str.replace(" ","|")
print(new_str)
new_str=new_str.split("|")
print(new_str)