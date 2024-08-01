# 函数返回值
def add(a,b):
    """
    add函数可以接受两个参数实现两数相加的功能
    :param a:其中一个参数
    :param b:另一个参数
    :return:相加的和
    """
    result = a + b
    return  result
r = add(1,3)
print(r)
# None类型
def say_hi():
    print("hi")
result = say_hi()
print(f"say_hi()返回的值是{result}")    #无返回值函数，返回值就是none
print(f"say_hi()返回的类型是{type(result)}")
# 函数的嵌套调用
def fun_b():
    print("2")
def fun_a():
    print("1")
    fun_b()
    print("3")
fun_a()
# 变量作用域
num = 100
def test_1() :
    global  num  #global 关键字，声明num是全局变量
    num = 200
test_1()
print(num)
# python数据容器
# 列表
# 黑马ATM
money = 5000000
name = input()
def balance() :
    print("-----------------------余额查询-----------------------")
    print(f"{name}，您好，您的余额剩余：{money}元")
def deposit(cash) :
    print("-----------------------存款-----------------------")
    print(f"{name},您好，您存款{cash}元成功")
    global money
    money = money + cash
    print(f"{name},您好，您的余额剩余：{money}元  ")
def withdrawal(cash) :
    print("-----------------------取款-----------------------")
    print(f"{name},您好，您取款{cash}元成功")
    global money
    money = money - cash
    print(f"{name},您好，您的余额剩余：{money}元")
def menu() :    #因为menu函数会用到前面的函数，所以放在最后写
    print("-----------------------主菜单-----------------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款     \t【输入2】")
    print("取款     \t【输入3】")
    print("退出     \t【输入4】")
    return int(input("请输入您的选择:"))
while True:   #设置无限循环，确保程序不会退出
    key_word = menu()
    if key_word == 1 :
        balance()
    elif key_word == 2 :
        cash = int(input("您想存入多少钱："))
        deposit(cash)
    elif key_word == 3 :
        cash = int(input("您想取出多少钱："))
        withdrawal(cash)
    elif key_word == 4 :
        exit()

