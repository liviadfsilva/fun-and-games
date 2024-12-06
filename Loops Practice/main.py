# # Printing odd numbers
# for i in range(100):
#     if i % 2 != 0:
#         print(i)
#
# # Printing even numbers
# for i in range (100):
#     if i % 2 == 0:
#         print(i)
#
# # Multiplication table
# number = 3
#
# for i in range(1, 11):
#     i *= number
#     print(i)

# # Countdown Timer
# number = int(input("What number do you want the countdown to start from?\n"))
#
# while number != 0:
#     print(number)
#     number -= 1

#Write a program that asks the user for a number N and prints all numbers from 1 to N using a while loop.

nr_choice = int(input("Choose the number you'd like to reach.\n"))

number = 0

while number < nr_choice:
    number += 1
    print(number)