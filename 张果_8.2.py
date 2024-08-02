#1
age=[21,25,21,23,22,20]
age.append(31)
print(f"追加一个数字31，到列表的尾部得：{age}")
age.extend([29,33,30])
print(f"追加一个新列表[29,33,30]，到列表的尾部得：{age}")
num1=age[0]
print(f"取出第一个元素为：{num1}")
num2=age[-1]
print(f"取出最后一个元素应为：{num2}")
weiz=age.index(31)
print(f"查找元素31，在列表中的下标位置为：{weiz}")
#2
list=[1,2,3,4,5,6,7,8,9,10]
len=len(list)
list2=[]
list3=[]
for x in range(0,len):
    if list[x]%2==0:
        list2.append(list[x])

print(f"新列表为{list2}(for循环)")
i=0
while i<len:
    if list[i] % 2 == 0:
        list3.append(list[i])
    i+=1

print(f"新列表为{list3}(while循环)")
#3
t=('周杰轮',11,['football','music'])
n1=t.index(11)
print(f"查询其年龄所在的下标位置为：{n1}")
n2=t[0]
print(f".查询学生的姓名为：{n2}")
del t[2][1]
print(f"删除学生爱好中的football后，元组为：{t}")
t[2].append('codinq')
print(f"增加爱好:codinq到爱好list内后为：{t}")
#4
string="itheima itcast boxuegu"
t1=string.count('it')
print(f"统计字符串内有{t1}个it字符")
t2=string.replace(" ","|")
print(f"被替换空格后:{t2}")
print(f"按照|分隔后，得到:{t2.split('|')}")
