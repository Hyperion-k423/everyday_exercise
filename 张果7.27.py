name="传智播客"
#公司名
stock_price=19.99
#当前股价
stock_code="003032"
#股票代码
stock_price_daily_growth_factor=1.2
#增长系数
growth_days=7
#增长天数
print(f"公司:{name}，股票代码:{stock_code}，当前股价:{stock_price}")
print("每日增长系数是:%.1f，经过%d天的增长后，股价达到了:%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price*(stock_price_daily_growth_factor**growth_days)))

user_name="黑马程序员"
#记录用户名称
user_type="SSSSSVIP"
#记录用户类型
print(f"您好:{user_name}，您是尊贵的:{user_type}用户，欢迎您的光临。")