# Write your code here 👇
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz") #if i is divisible by 3 & 5, print FizzBuzz.
    elif i % 3 == 0:
        print("Fizz") #if i is divisible by 3, print Fizz.
    elif i % 5 == 0:
        print("Buzz") #if i is divisible by 5, print Buzz.
    else:
        print(i) # else, print the plain number.
̄