height = float(input("请输入您的身高（单位：米）："))
weight = float(input("请输入您的体重（单位：千克）："))

bmi =  weight / (height ** 2)

print("您的BMI值为：", round(bmi,2))

if bmi < 18.5:
    print("您的体重偏轻，建议增加营养摄入。")
elif 18.5 <= bmi and bmi < 24:
    print("您的体重正常，继续保持健康的生活方式。")
elif 24 <= bmi and bmi < 28:
    print("您的体重过重，建议控制饮食和加强锻炼。")
else:
    print("您的体重肥胖，建议寻求医生或营养师的帮助，制定合适的减重计划。")