name1 = str(input("Enter first person's name:  "))
name2 = str(input("Enter first person's name:  "))
a = name1.upper()
b = name2.upper()
sum = 0
sum1 = 0
sum += a.count("T")
sum += a.count("R")
sum += a.count("U")
sum += a.count("E")
sum += b.count("T")
sum += b.count("R")
sum += b.count("U")
sum += b.count("E")

sum1 += a.count("L")
sum1 += a.count("O")
sum1 += a.count("V")
sum1 += a.count("E")
sum1 += b.count("L")
sum1 += b.count("O")
sum1 += b.count("V")
sum1 += b.count("E")

new1 = str(sum)
new2 = str(sum1)
new3 = int(new1 + new2)

if not (not (new3 < 10) and not (new3 > 90)):
    print(f"Your score is {new3}, you go together like coke and mentos.")
elif 40 < new3 < 50:
    print(f"Your score is {new3}, you are alright together.")
else:
    print(f"Your score is {new3}.")
