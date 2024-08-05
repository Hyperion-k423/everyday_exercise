# 数据容器的切片
# 序列（内容连续、有序、可使用下标索引的一类数据容器，元组、列表、字符串都是）
    # 对list进行切片    从起始下标开始，到末尾下标结束（不含），
my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]   #步长默认为1，可省略不写
print(result1)
    # 对tuple进行切片
my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:]   #起始和结尾下标不写，表示从头到尾。步长不写默认为1
print(result2)
    #对str进行切片
my_str = "0123456"
result3 = my_str[::2]   #起始和结尾下标不写，表示从头到尾，步长为二
print(result3)
    #对str进行切片，步长为-1
result4 = my_str[::-1]
print(result4)      #相当于反转了序列
    #对列表进行切片
result5 = my_list[3:1:-1]   #倒着切片
print(result5)
    #对元组倒着进行切片
result6 = my_tuple[::-2]
print(result6)
# 集合（ 无序，去重 ）
my_set = {"li","xiao","man","li","xiao","man","li","xiao","man"}
my_set_empty = set()   #定义空集合
print(f"my_set的内容是：{my_set},类型是{type(my_set)}")
print(f"my_set的内容是：{my_set_empty},类型是{type(my_set_empty)}")
    #添加新元素 .add方法
my_set.add("bian")
my_set.add("man")
print(my_set)
    #移除元素  .remove
my_set.remove("man")
print(my_set)
    #随机取出元素    .pop
element = my_set.pop()
print(f"取出的元素是{element},取出后的集合是{my_set}")
    #清空方法   .clear
my_set.clear()
print(my_set)
    #取两个集合的差集方法 .difference()
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)   #取出set1里有的但set2里没有的
print(f"取出差集后的结果是{set3}")
    #消除两个集合的差集
set1.difference_update(set2)
print(f"消除差集后，集合1结果{set1}")
print(f"消除差集后，集合2结果{set2}")
    #两个集合合并的方法 .union
set3 = set1.union(set2)
print(f"两个集合合并后的结果{set3}")
    #len()函数统计集合元素内数量
num_set = {1,1,2,3,4,5}
print(f"集合内元素个数是{len(num_set)}")
    #用for循环遍历
for element in num_set :        #因为无法使用下标索引，所以无法用while循环遍历
    print(f"集合内的元素有{element}")


#字典{key:value}
my_dict = {"王力宏" : 99,"周杰伦": 88,"林俊杰":77}
my_dict2 = {}   #定义空字典（因为{}这个形式被空字典占用了，所以空集合用set()）
                     #也可以这样定义my_dict2 = dict()
print(f"字典1的内容是{my_dict},类型是{type(my_dict)}")
    #key不可以重复，新的会把老的覆盖掉
my_dict = {"王力宏" : 99,"王力宏" : 88,"周杰伦": 88,"林俊杰":77}
print(f"字典1的内容是{my_dict}")
    #基于key得到value
score = my_dict["王力宏"]
print(f"王力宏的分数是{score}")
    #字典的嵌套
stu_score_dict = {
    "tom":{
        "语文" : 99,
        "数学" : 88,
        "英语" : 77,
    },"bin":{
        "语文": 98,
        "数学": 89,
        "英语": 78,
    },"john":{
        "语文": 98,
        "数学": 87,
        "英语": 75,
    }
}
    #从嵌套字典中获得数据
print(f"john的语文分数是{stu_score_dict["john"]["语文"]}")
    #字典的常用操作
    #增加新元素
my_dict = {"王力宏" : 99,"周杰伦": 88,"林俊杰":77}
my_dict["张学友"] =66
print(f"增加后的字典为{my_dict}")
    #更新元素
my_dict["周杰伦"] = 33
print(f"更过更新后{my_dict}")
    #删除元素
score = my_dict.pop("周杰伦")
print(f"字典中被移除一个元素，结果{my_dict},周杰伦的分数是{score}")
    #清空元素
my_dict.clear()
print(my_dict)
    #获取全部key
my_dict = {"王力宏" : 99,"周杰伦": 88,"林俊杰":77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")
    #遍历字典
for key in keys :    #for key in my_dict  也可以
    print(f"字典的key是{key}")
    print(f"字典的value是{my_dict[key]}")
    #统计字典内的元素数量
mount = len(my_dict)
print(f"字典中元素数量是{mount}")
# 8- 3序列的切片实践
strr = "万过薪月，员序程马黑来，nohtyP学"
fanzhuan = strr[::-1]
fanzhuan2 = fanzhuan[9:14]
print(fanzhuan2)
"""
    可以这样写
        result = strr[::-1][9:14]
        print(result)
 """
# 8-3 信息去重
my_list = ["黑马程序员","传播智客","黑马程序员","传播智客","itheima","itcast","itheima","itcast","best"]
set_zero = set()
for element in my_list:
    print(f"my_list中的元素有{element}")
    set_zero.add(element)
print(set_zero)
#8-3升职加薪
my_dictX = {
    "王力宏":{
    "部门":"科技部",
    "工资":3000,
    "级别":1
    },
    "周杰伦":{
    "部门":"市场部",
    "工资":5000,
    "级别":2
    },
    "林俊杰":{
    "部门":"市场部",
    "工资":7000,
    "级别":3
    },
    "张学友":{
    "部门":"科技部",
    "工资":4000,
    "级别":1
    },
    "刘德华":{
    "部门":"市场部",
    "工资":6000,
    "级别":2
    }
}
for name in my_dictX :
    if my_dictX[name]["级别"] == 1:
        employee = my_dictX[name]
        employee["级别"] = 2
        employee['工资'] += 1000
        my_dictX[name] = employee
print(f"对员工进行升职加薪后的结果是{my_dictX}")
