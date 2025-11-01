usd_rate = 0.1383
jpy_rate = 20.6902
krw_rate = 288.86

rmb = float(input("请输入人民币金额："))
usd = rmb * usd_rate
jpy = rmb * jpy_rate
krw = rmb * krw_rate

print(f"{rmb}人民币可以兑换为：\n 美元：{usd:.2f}\n 日元：{jpy:.2f}\n 韩元：{krw:.2f}")