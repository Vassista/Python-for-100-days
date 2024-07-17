import random

rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock,paper,scissors]
computer_choice = random.choice(choices)
user_choice = choices[int(input("Enter 0 for rock, 1 for paper, 2 for scissors"))]

if user_choice == rock and computer_choice == paper:
    print('Your choice : \n' + user_choice)
    print("Computer choice: \n" + computer_choice)
    print("You loose!")

elif user_choice == paper and computer_choice == scissors:
    print('Your choice : \n' + user_choice)
    print("Computer choice: \n" + computer_choice)
    print("You loose!")

elif user_choice == scissors and computer_choice == rock:
    print('Your choice : \n' + user_choice)
    print("Computer choice: \n" + computer_choice)
    print("You loose!")

elif user_choice == computer_choice:
    print('Your choice : \n' + user_choice)
    print("Computer choice: \n" + computer_choice)
    print("It's a tie!")

else:
    print('Your choice : \n' + user_choice)
    print("Computer choice: \n" + computer_choice)
    print("You Win!!")

