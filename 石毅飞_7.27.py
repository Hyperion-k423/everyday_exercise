name = "传智播客1"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name},股票代码：{stock_code}，当前股价：{stock_price}")
stock_price = stock_price *stock_price_daily_growth_factor**growth_days
print("每日增长系数：%.2f，经过%d天的增长后，股价达到了%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price))




user_name = "黑马程序员"
user_type = "SSSSSVIP"
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎下次光临")