# 列表的下标索引
my_list = [[1,2,3],[3,4,5]]
print(my_list[1][2])
    # 列表的常用操作
    # 列表中的方法
    # .index 查找列表中元素的下标索引
list_2 = ["a","b","c"]
index = list_2.index("a")
print(f"list_2中,'a'的下标索引值是{index}")
    # 修改元素
list_2[0] = "f"
print(list_2[0])
    # .insert插入元素
list_2.insert(1,"g")
print(list_2)
    # .append 在列表末尾追加元素
list_2.append("h")
print(list_2)
    # .extend在列表末尾追加一个列表
list_3 = ["q","w","e"]
list_2.extend(list_3)
print(list_2)
    # 删除元素
del list_2[0]    #用关键字del删除
print(list_2)
element = list_2.pop(0)   # 通过方法pop取出元素
print(f"通过pop方法取出元素后列表内容为{list_2},取出的元素是{element}")
list_2.remove("e")  #指定一个元素然后去除
print(list_2)
    # 清空列表
list_2.clear()
print(list_2)
    # .count方法统计列表中某一元素的数量
num = list_2.count("b")
print(num)   #上一步中列表被清空了
    # len()函数统计列表中一共有多少元素
count = len(list_2)
print(count)
    # 列表的遍历
    #用while遍历列表
name = ["li","xiao","man"]
index = 0
while index < len(name):
    element = name[index]
    print(f"列表的第{index + 1}个元素：{element}")
    index += 1
    # 用for遍历列表
for element in name :
    print(f"列表的元素有：{element}")


# 元组tuple  （元组中的数据不能被修改）
t1 = (1,"hi",True)     #定义一个元组
t2 = ()    # 定义一个空元组
t3 = tuple()   # 定义一个空元组
print(f"t1的类型是{type(t1)},内容是{t1}")
t4 = ((1,2,3),(3,4,5))   #tuple的嵌套
num = t4[1][1]
print(f"从嵌套元组中取出的元素是{num}")
    # 元组的操作
    # 1. .index方法
num = t4.index((1,2,3))     #但是怎么取出嵌套中的单个元素呢？
print(f"{num}")
    # 2. count统计方法
num = t4.count((1,2,3))
print(f"{num}")
    # 3. len函数
num = len(t4)
print(f"{num}")
    # 遍历元组
index = 0
while index < len(t1) :
    print(f"元组t1的元素有{t1[index]}")
    index += 1
for element in t1 :
    print(f"元组t1的元素有{element}")
    # 元组与列表的嵌套
t6 = (1,2,["hi","man"])
t6[2][0] = "Hi"
t6[2][1] = "Man"
print(f"t6的内容是{t6}")  # 元组不可改变，但元组中嵌套的列表中的元素可以改变



# 字符串
my_str = "LiXiaoMan"
print(f"my_list中的第三个元素是{my_str[2]}")
    # my_str[2] = "x"这种写法是错误的，字符串不能被修改
value = my_str.index("Xiao")
print(f"在字符串{my_str}中查找Xiao，其起始下标是：{value}")
    #replace方法
new_my_str = my_str.replace("Li","li")    #将原来字符串中的所有“Li”都替换为“li”
print(f"将字符串{my_str}替换为{new_my_str}")
    # .split字符串的分割
my_str = "li xiao man"
my_str_list = my_str.split(" ")     #通过空格符号来切分字符串,得到一个列表
print(f"将字符串{my_str}进行split切割后，得到一个列表{my_str_list},类型是{type(my_str_list)}")
    # .strip字符串的规整操作
my_str = "  lixiaoman  "
print(f"{my_str.strip()}")    #未向.strip方法传递参数，用于去除字符串中的前后空格
my_str = "10lixiaoman01"
print(f"{my_str.strip("10")}")    #向.strip方法传递参数“10”，用于去除字符串中的"1"和"0"元素
    # .count方法统计字符串中某字符串出现的次数
print(f"字符串{my_str}中，字符串i出现的次数是{my_str.count("i")}")
    # len()函数统计字符串的长度
print(f"字符串{my_str}的长度是{len(my_str)}")


# 8-2常用功能练习
numlist = [21,25,21,23,22,20]
numlist.append(31)
numlist.extend([29,33,30])
numlist.pop(0)
numlist.pop(-1)
number = numlist.index(31)
print(number)
# 8-2取出列表内偶数
num_list = [1,2,3,4,5,6,7,8,9,10]
even_number=[]
index = 0
while index < len(num_list) :
    if num_list[index] % 2 ==0 :
        even_number.append(num_list[index])
    index += 1
print(f"通过while循环，从列表：[1,2,3,4,5,6,7,8,9,10]中取出偶数，组成新列表{even_number}")
for count in num_list :    # for循环，令count挨个等于num_list中的元素
    if count % 2 == 0:
        even_number.append(count)
print(f"通过for循环，从列表：[1,2,3,4,5,6,7,8,9,10]中取出偶数，组成新列表{even_number}")
# 8 - 2元组的基本操作
Tx = ("周杰伦",11,["football","music"])
print(f"年龄所在的下标位置为{Tx.index(11)}")
print(f"查询学生的姓名{Tx[0]}")
del Tx[2][0]    #删除学生爱好中的football
print(Tx)
Tx[2].insert(0,"coding")  #在元组的列表中增加元素
print(Tx)
# 8-2分割字符串
strr = "itheima itcast boxuegu"
print(f"字符串{strr}中有：{strr.count("it")}个it字符")
new_my_str = strr.replace(" ","|")
print(f"字符串{strr}中，被替换空格后，结果：{new_my_str}")
print(f"字符串{strr}中,按照|分隔后得到：{new_my_str.split("|")}")

