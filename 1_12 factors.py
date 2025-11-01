def print_factors(number):
    print(f"求解{number}的因子：")
    for i in range(1,number + 1):
        if number % i == 0:
            print(i, end="")
    print()
num = int(input("请输入一个正整数："))
print_factors(num)