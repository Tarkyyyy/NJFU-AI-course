print("1~10之间所有偶数的平方：")
for num in range(1,11):
    if num % 2 == 0:
        square = num ** 2
        print(f"{num}的平方是：{square}")