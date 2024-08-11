class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # str魔术方法
    def __str__(self):
        return f"Student类对象，name：{self.name},age{self.age}"
    # lt魔术方法
    def __lt__(self,other):
        return self.age<other.age
    # le魔术方法
    def __le__(self,other):
        return self.age<=other.age
    # ed魔术方法
    def __eq__(self, other):
        return self.age==other.age

stu1=Student("zhou",31)
stu2=Student("lin",36)
print(stu1)
print(str(stu1))
print(stu1<stu2)
print(stu1<=stu2)
print(stu1==stu2)

