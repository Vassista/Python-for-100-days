# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

print(f"The highest score in the class is: {max(student_scores)}")

#alternate version:
# max = 0
# for i in student_scores:
#   if i > max:
#     i,max = max,i
# print(f"Thē highest score in the class is: {max}").