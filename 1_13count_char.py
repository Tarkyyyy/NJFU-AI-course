
def count_char(text, char='a'):
    count = text.count(char)
    return count

text = input("请输入一个字符串：")
usr_char = input("请输入要统计的字符（留空则使用默认字符‘a’）：")

if usr_char:
    result = count_char(text,usr_char)
else:
    usr_char = 'a'
    result = count_char(text)
print(f"字符’{usr_char}'在字符串中出现了{result}次")