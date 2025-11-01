def arith_calcu():
    num1 = float(input("请输入第一个数字："))
    operator = input("请输入运算符（+，-，*，/）：")
    num2 = float(input("请输入第二个数字："))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("错误：除数不能为0！")
            return
        result = num1 / num2
    else:
        print("未知的运算符！")
        return
    print(f"{num1} {operator} {num2} = {result}")
arith_calcu()
