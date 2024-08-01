#7.27-1
name="传智播客"
stock_price=19.99
stock_code="003032"
stock_price_daily_growth_factor=1.2
growth_days=7
finally_stock_price=stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%.1f"%(stock_price_daily_growth_factor),"经过%d"%growth_days,"天的增长后，股价达到了：%.2f"%finally_stock_price)
#7.27-2
#数据输入input
"""
name=input()默认接收字符串类型
"""
user_name=input("你的名字")
user_type=input("您的VIP LV")
print("您好：%s,"%(user_name),"您是尊贵的:%s用户，欢迎您的光临。"%(user_type))

