name = "传智博客"
stock_price = 19.99
stock_code = "003032"
factor = 1.2
growth_days = 7
total =("公司:%s,股票代码:%s,当前股价:%f" % (name, stock_code, factor) +
        "每日增长系数是:%s,经过%s天的增长后,股价达到了:71.63" % (factor, growth_days))
print(total)
user_name = "黑马程序员"
user_type = "SSSSSVIP"
print("%s,您是尊贵的：%s用户，欢迎您的光临" % (user_name, user_type))
