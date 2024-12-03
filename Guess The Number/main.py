import random

answer = random.randint(1,101)

while True:
    guess = int(input("Guess the number, from 1 to 100.\n"))

    if guess > answer:
      print("Too high. Try again.")
    elif guess < answer:
       print("Too low. Try again.")
    else:
      print(f"You did it! The correct number is {answer}.")