asian_record = 46.97
world_record = 26.40

input_time = float(input("请输入您的游泳成绩（单位：秒）："))

if input_time < world_record:
    print("恭喜！您打破了男子100米自由泳的世界纪录！")
else:
    if input_time < asian_record:
        print("恭喜！您打破了男子100米自由泳的亚洲纪录！")
    else:
        print("很遗憾，您的成绩未能打破记录。")