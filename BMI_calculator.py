height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round((weight/(height**2)), 2)


if BMI < 18.5:
    print(f"your BMI is {BMI}, you are UNDERWEIGHT")
elif BMI < 25:
    print(f"your BMI is {BMI}, you have a NORMAL WEIGHT")
elif BMI < 30:
    print(f"your BMI is {BMI}, you have a OVERWEIGHT")
elif BMI < 35:
    print(f"your BMI is {BMI}, you OBESE")
else:
    print(f"your BMI is {BMI}, you are CLINICALLY OBESE")
