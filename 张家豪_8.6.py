#异常：Bug，就是出错了
"""
    捕获异常
        try:
            可能发生的错误代码
        except:
            如果出现异常执行的代码
"""
try:
    f = open("D:/abc.txt","r",encoding="UTF-8")
except :
    print("出现异常了，因为文件不存在，所以要将open的打开模式改变为'w")
    f = open("D:/abc.txt","w",encoding="UTF-8")
    #捕获指定异常
try :
    print(name)
except NameError as e:         #NameError是一种异常类型
    print("出现了变量未定义的异常")
    print(e)
    #捕获多个异常
try :
    print(name)
     #1 / 0
except (NameError , ZeroDivisionError) as e :
    print("出现了变量未定义 或者 除以0的异常错误")
    #捕获所有异常
try :
    1/0
except Exception as e:     #尽量用这个就行
    print("出错了")
        #异常else：没有异常时要执行的代码
try :
    1/0
except Exception as e:     #尽量用这个就行
    print("出错了")
else :
    print("HappyHappy")
    #finally：无论有没有异常都要执行的代码
try:
    f = open("D:/abc.txt","r",encoding="UTF-8")
except :
    print("出现异常了，因为文件不存在，所以要将open的打开模式改变为'w")
    f = open("D:/abc.txt","a",encoding="UTF-8")
    f.write("asd")
finally:
    f.close()


#异常的传递性
    #定义一个出现异常的方法
def func_1():
    print("func_1 开始执行")
    num = 1 / 0       #异常最先出现的地方
    print("func_1 结束执行")
def func_2():
    print("func_2 开始执行")
    func_1()
    print("func_2 结束执行")
def main():
    try:
        func_2()
    except Exception as e:
        print(f"出现异常了，异常的信息时{e}")     #这里启示我们发现异常并不用找到异常最先出现的地方
main()


#模块：一个python文件，可以帮助实现一些功能，可理解为功能包
    #模块的导入   [from 模块名] import [模块 | 类 | 变量 | 函数 | * ] [as 别名 ]     []中的内容是选写
        #示例导入time模块
import time
time.sleep(5)       # . 说明sleep()是属于time模块的。通过 . 使用模块中的功能
print("hi")
        #另一种方法
from time import  sleep      #这样只能使用sleep功能
sleep(3)
print("hello")
        #使用*导入模块中全部功能
from time import  *
sleep(2)                  #这样就不用 . 来使用功能了
print("everyone")
        #模块别名
import  time as tt     #用于给名字很长的模块一个简单别名
tt.sleep(2)
print("over")

#自定义模块
# my_moudel.test(2,3)
    #导入不同模块的同名功能
import  my_moudel2
my_moudel2.test(2,3)
    #__main__变量，__main__变量下的内容只能在本文件中运行
from my_moudel import  test
test(1,5)       #会发现my_moudel中的test(1,5)并没有被调用
    #__all__变量：在使用 import *的时候，只会调用__all__下的内容
from my_moudel import *
test_a(3,8)



#python包：物理上来看，就是一个文件夹，该文件夹一定包含一个_init_.py 类型的文件。
    #自定义包
        #以下这几种导入方式都是可以的
import test.my_module1
import test.my_module2
test.my_module1.info_print1()
test.my_module2.info_print2()
from test import my_module1
my_module1.info_print1()
from test import my_module2
my_module2.info_print2()
from test.my_module1 import info_print1
info_print1()
        #通过__all__变量控制import*
from test import *
my_module1.info_print1()
    #安装第三方包
