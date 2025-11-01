height = float(input("请输入您的身高（单位：米）："))
weight = float(input("请输入您的体重（单位：千克）："))

bmi =  weight / (height ** 2)

print("您的BMI值为：", round(bmi,2))