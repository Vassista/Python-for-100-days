#If the bill was $150.00, split between 5 people, with 10% or 12% or 15%  tip. 
#Format the result to 2 decimal places = 33.60
#Write your code below this line 👇
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = tip_percentage/100 * bill
bill += tip
total_people= int(input("How many people to split the bill? "))
each_person_bill = round(bill / total_people,2)
print(f"Each person should pay: ${each_person_bill:.2f}") ## The `:.2f` part of the expression is a format specifier that specifies the precision of the floating-point number