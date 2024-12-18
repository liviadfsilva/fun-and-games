import random

rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
        ________
---'    ________)
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
---.___________
        _______)
---.________)
'''

spock = '''
    ⌠⌒|  ◜﹆◜﹆
 ⌠⌒⌉| | / // /
 |_|| | /-//=/
 | || |/ // /
 | || | // /
           ______
 |         ______)
 |       |
'''

shapes = [rock, paper, scissors, lizard, spock]

user_choice = int(input("What do you choose?\n"
      "Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard or 4 for Spock.\n"))

if user_choice >= 0 or user_choice <= 4:
      print(shapes[user_choice])

computer_choice = random.randint(0,4)
print("Computer chose:")
print(shapes[computer_choice])

if user_choice > 4 or user_choice < 0:
      print("You typed an invalid option.")
elif user_choice == computer_choice:
      print("It's a draw.")
elif user_choice == 0 and computer_choice == 2 or computer_choice == 3:
      print("You win!")
elif user_choice == 1 and computer_choice == 0 or computer_choice == 4:
      print("You win!")
elif user_choice == 2 and computer_choice == 1 or computer_choice == 3:
      print("You win!")
elif user_choice == 3 and computer_choice == 1 or computer_choice == 4:
      print("You win!")
elif user_choice == 4 and computer_choice == 0 or computer_choice == 2:
      print("You win!")
else:
      print("You lose!")