
height = input("enter your height in in: ")
weight = input("enter your weight in lbs: ")

height_converted = int(height)
weight_converted = int(weight)

bmi = weight_converted * 703 / height_converted ** 2

bmi_whole_number = int(bmi)

print(bmi_whole_number)











