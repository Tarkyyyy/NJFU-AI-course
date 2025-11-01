name = input("请输入你的姓名：")
city = input("请输入你来自的城市：")
current_time = int(input("请输入当前时间的小时部分（0~23）："))

if 5 <= current_time < 12:
    greeting_prefix = "早上好"
elif 12 <= current_time < 18:
    greeting_prefix = "下午好"
else:
    greeting_prefix = "晚上好"

greeting= f"{greeting_prefix}，{name}！来自{city}的你今天过得怎么样？"
print(greeting)