target = int(input())  # Enter a number between 0 and 1000.̄
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum = 0
for i in range(2, target + 1, 2):
    sum += i
print(sum)
