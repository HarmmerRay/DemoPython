name = "迈思科技"
stock_price = 18.88
stock_code = '668888'
stock_price_daily_growth_factor = 1.88
growth_days = 7

print("公司：%s , 股票代码为%s" % (name, stock_code))
print(f"当前股票价格{stock_price},股票增长系数为:{stock_price_daily_growth_factor},"
      f"经过{growth_days}天的增长,当前股票价格 %.2f" % (stock_price * (stock_price_daily_growth_factor ** growth_days)))
print("1.2的7次方")
