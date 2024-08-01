name = 'man' # 单引号定义字符串
name = "man" # 双引号定义字符串
name = """"man""" # 三引号定义字符串
print(type(name))
# 在字符串内包含双引号
name = '"黑马程序员"'
print(name)
name = " '河马程序员' "
print(name)
name = "\"黑马程序员\""
print(name)
# 字符串拼接
print("man " + "what can i say")
first = "man"
sec = "what can i say"
print(first + sec)
# 字符串格式化
name = "man"
message = "%s , what can i say" % name
print(message)
class_num = 1
avg_salary = 8000
message = "第 %s 期，平均工资：%s" %(class_num,avg_salary) # %s将内容转换为字符串进行占位
print(message)
message = "第 %d 期,平均工资 %f " % (class_num,avg_salary) # %d将内容转换为整数进行占位；%f将内容转换为浮点数进行占位
print(message)
# 字符串格式化2
event = "中华人民共和国成立了"
year = 1949
print(f"{year},年{event}") # f"{占位}"
# 对表达式进行格式化
# 表达式：一条具有具体执行结果的语句
print("1 + 1 的结果是 %d" %(1+1)) # %s/d/f  %(表达式)
print(f"1 + 1 的结果是 {1+1}") # f"{表达式}"
# 数据输入 input()
print("who are you")
name = input()
print("I am ",name)
name = input("请告诉我你是谁\n") # 提示语句直接写到input的括号里
print("i am %s" % name)
num = input("请告诉我你的银行卡密码\n")
num = int(num) # input()输入的都是字符串类型，想要转换为其他类型需要自己动手
print("你的银行卡密码是 %d" %(num))
# 7.27练习股价计算
name = "传播智客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司名称：{name}, 股票代码：{stock_code}, 当前股价：{stock_price }")
print("每日增长系数是：%.1f,经过%d 天增长后，股票达到了%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price_daily_growth_factor ** growth_days * stock_price))
#7.27练习_欢迎登录小程序
user_name = input()
user_type = input()
print(f"{user_name},您是尊贵的{user_type}用户，欢迎您的光临")


