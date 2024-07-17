# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight / height ** 2)
#Under 18.5 they are underweight
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
#Between 18.5 and 25 they have a normal weight
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
#Between 25 and 30 they are slightly overweight
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")
#Between 30 and 35 they are obese
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
#Above 35 they are clinically obese
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
