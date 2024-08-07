#五类容器的通用操作
    #都支持遍历操作
    #len(容器)    ：统计容器的元素个数
        #例如：len(my_dict)
    #max(容器)    ：统计容器内最大元素
        #例如：max(my_list)
    #min(容器)    :统计容器内最小元素
        #例如：min(my_tuple)
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
    #len()统计个数
print(f"列表中元素的个数是：{len(my_list)}")
print(f"元组中元素的个数是：{len(my_tuple)}")
print(f"字符串中元素的个数是：{len(my_str)}")
print(f"集合中元素的个数是：{len(my_set)}")
print(f"字典中元素的个数是：{len(my_dict)}")
    #max()最大元素
print(f"列表中的最大元素是：{max(my_list)}")
print(f"元组中的最大元素是：{max(my_tuple)}")
print(f"字符串中的最大元素是：{max(my_str)}")
print(f"集合中的最大元素是：{max(my_set)}")      #字符串中怎么找最大呢？
print(f"字典中的最大元素是：{max(my_dict)}")
    #min()最小元素
print(f"列表中的最小元素是：{max(my_list)}")
print(f"元组中的最小元素是：{max(my_tuple)}")
print(f"字符串中的最小元素是：{max(my_str)}")
print(f"集合中的最小元素是：{max(my_set)}")
print(f"字典中的最小元素是：{max(my_dict)}")
    #类型转换：容器转列表
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")   #value被舍弃了只剩下了key
    #类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")    #value被舍弃了只剩下了key
    #类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")     #双引号都被省略了
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")
    # 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")  #数据无序
print(f"字典转集合的结果是：{set(my_dict)}")   #数据无序
    #通用排序功能  sorted(容器)
my_list = [3,4,1,2,5]
my_tuple = (3,2,1,4,5)
my_str = "cabedg"
my_set = {3,2,5,4,1}
my_dict = {"key1":4,"key2":2,"key3":1,"key4":5,"key5":3}
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")
    #反向排序   sorted(容器，reverse = True)
print(f"列表对象的排序结果：{sorted(my_list,reverse=True)}")
print(f"元组对象的排序结果：{sorted(my_tuple,reverse=True)}")
print(f"字符串对象的排序结果：{sorted(my_str,reverse=True)}")
print(f"集合对象的排序结果：{sorted(my_set,reverse=True)}")
print(f"字典对象的排序结果：{sorted(my_dict,reverse=True)}")
    #字符串的大小比较：ASCII码表
print(f"abb大于aaa的结果是{'abb' > 'aaa'}")   #一位一位的比较，其中一位大，整体就大


#函数的多个返回值
def test_return():
    return 1,2,"hi"
x,y,z = test_return()
print(x)
print(y)
print(z)
#函数的多种传参方式
def user_info(name,age,gender):
    print(f"您的名字是：{name},年龄是：{age}，性别是：{gender}")
    # 关键字传参
user_info(name = "小明",age = 19, gender = "男")
        # 可以不按照固定顺序
user_info(age = 19,name= "小明", gender= "男")
        # 可以和位置参数混用，但位置参数必须在前，切匹配参数顺序
user_info("小明",age= 19,gender= "男")
    #缺省参数
def user_info(name,age,gender = "男"):
    print(f"您的名字是：{name},年龄是：{age}，性别是：{gender}")
user_info("小满",19)
        #也可以覆盖
user_info("小满",13,"女")
    #不定长的参数
        #位置不定长，*；不定长定义的形式参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args) :
    print(f"args参数的形式是{type(args)},内容是{args}")
user_info("w",1,0,"女孩")
        #关键字不定长，**；  key = word
def user_info(**kwargs) :
    print(f"kwargs参数的形式是{type(kwargs)},内容是{kwargs}")
user_info(name = "小满",age = 19 , gender = "男")



#匿名函数
    #定义一个函数，接收另一个函数作为传入参数
def test_func(compute) :
    result = compute(3,4)  #确定compute是函数
    print(type(compute))
    print(f"计算结果{result}")
def compute(x,y):
    return  x+y
test_func(compute)