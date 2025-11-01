user_input = input("请输入一个字符串：")
a_count = e_count = i_count = o_count = u_count = 0
for char in user_input:
    if char.lower() == 'a':
        a_count += 1
    elif char.lower() == 'e':
            e_count += 1
    elif char.lower() == 'i':
            i_count += 1
    elif char.lower() == 'o':
            o_count += 1
    elif char.lower() == 'u':
            u_count += 1

print("元音字母出现的次数：")
print("a:", a_count)
print("e:", e_count)
print("i:", i_count)
print("o:", o_count)
print("u:", u_count)

