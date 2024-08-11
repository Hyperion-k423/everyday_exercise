#设计一个类：类比生活中设计一个表格
"""
    class 类名称:
        类的属性：定义在类中的变量
        类的行为：定义在类中的函数。方法就是类内部的函数
"""
class Student:
    name = None  #记录学生姓名
    gender = None   #记录性别
    nationality = None      #记录国籍
    native_place = None     #记录籍贯
    age = None  #记录年龄
#创建一个对象（类比生活中打印一张登记表）
stu_1 = Student()
#对象属性赋值（填写表单）
stu_1.name = "李小满"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "河南"
stu_1.age = 19
#获取对象中记录的信息
print(stu_1.name)
print(stu_1.native_place)
print(stu_1.nationality)
print(stu_1.gender)
print(stu_1.age)


#定义类中的方法
class Student:
    name = None
    def say_hi(self):       #调用方法时，self不用传参
        print(f"大家好，我是{self.name}")     #self.name，这样才能访问name
    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")
stu = Student()
stu.name = "网易零"
stu.say_hi()
stu.say_hi2("我吗")

#构建一个闹钟类
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
    #创建一个对象
clock1 = Clock()
clock1.id = "lixiaoman"
clock1.price = 19
print(f"闹钟的名字是{clock1.id},价格是{clock1.price}")
clock1.ring()

#__init__()方法，被称之为构造方法
    #在创建类对象时，会自动执行
    #在创建类对象时，将传入参数自动传递给__init__方法使用
class Human:
    name = None
    age = None
    tel = None
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Human类创建了一个类对象")
human = Human("xiaoman",18,12312312)
print(human.name)
print(human.age)
print(human.tel)

#8-9 学生信息录入
class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
num_list = [1,2,3,4,5,6,7,8,9,10]
for num in num_list:
    print(f"当前录入第{num}位学生信息，总共录入10位学生信息")
    stu = Student(input("请输入学生姓名"),input("请输入学生年龄"),input("请输入学生地址"))
    print(f"学生{num}信息录入完成，信息为：【学生姓名：{stu.name},学生年龄：{stu.age},学生地址：{stu.address}")

#魔术方法：形如：__魔术__()
    #字符串方法：__str__()
    class Student:
        def __init__(self, name, age, address):
            self.name = name
            self.age = age
            self.address = address
        def __str__(self):
            return f"Student类对象，name：{self.name},age:{self.age}"
stu = Student("周杰伦",12,"河南")
print(stu)
print(str(stu))

#封装
    #私有成员
        #私有成员变量：变量名以__开头
        #私有成员方法：方法名以__开头
class Phone:
    __current_voltage = None
    def __keep_single_core(self):
        print("让CPU保持以单核模式运行")
phone = Phone()
# phone.__keep_single_core 这样是不行的
# print(phone.__current_voltage) 这样也是不行的
#私有成员不是给类对象使用的，而是给类中的其他成员（变量、方法等）使用的
#8-9设计带有私有成员的手机
class Phone:
    __is_5g_enable = bool   #为什么这里设置为bool之后，就一直被判定为True
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else :
            print("5g关闭，使用4g网络")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
vivo = Phone()
vivo.call_by_5g()