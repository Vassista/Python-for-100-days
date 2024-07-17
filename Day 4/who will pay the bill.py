import random
# Assuming names_string is input from the user
names_string = input("Enter names separated by a comma and space: ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
person = random.choice(names)
print(f"{person} will pay for the bill today!")