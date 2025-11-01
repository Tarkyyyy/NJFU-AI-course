original_string = input("请输入一串需要加密的字符串：")
encrypted_string = ""

for char in original_string:
    upper_char = char.upper()
    if 'A' <= upper_char <= 'Z':
        offset = ord(upper_char) - ord('A') + 2
        if offset > ord('Z'):
            offset -= 26
        encrypted_char = chr(ord('A') + offset)
    else:
        encrypted_char = char
    encrypted_string += encrypted_char
print("原始字符串：", original_string)
print("加密后的字符串：", encrypted_string)