# 7.27

# 字符串的三种定义方式 单，双，三引号
# 转义字符\解除引号的效用
name = "\"无畏契约\""
print(name)

# 字符串拼接 +号完成 不能让字符串和其他类型拼接，例如数字等
print("无畏契约" + "好玩")
name = "无畏契约"
x = "好玩"
print("谁：" + name + "怎样：" + x)

# 字符串格式化 %s %d %f
name = "无畏契约"
message = "好玩%s" % name
print(message)
num = 666
message = "%s好玩%s" % (name,num)
print(message)
# 快速格式化：f"{占位}"
name = "无畏契约"
x = 666
y = 6.66
print(f"{name},好玩，{x}{y}")


# 练习1
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print("公司：%s，股票代码：%s，当前股价：%s" % (name,stock_code,stock_price))
print(f"每日增长系数:{stock_price_daily_growth_factor},经过七天的增长后，股价达到了：{finally_stock_price}")

# 练习2
user_name = input("记录用户名称")
user_type = input("记录用户类型")
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎您的光临。")