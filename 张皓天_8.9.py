class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        for x in range(1, 11):
            print(f"当前录入第{x}位学生信息，总共需录入10位学生信息")
            student = Student(input("请输入学生姓名"), input("请输入学生年龄"), input("请输入学生地址"))
            print(f"学生{x}信息录入完成，信息为：【学生姓名：{student.name}年龄：{student.age},地址{student.address}")


class Phone:
    __is_5g_enable = True

    def __cheak_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__cheak_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()



