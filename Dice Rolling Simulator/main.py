from random import randint
from art import logo

def one_dice():
    print(logo)
    dice = randint(1, 6)
    print(f"Dice: {dice}")

def two_dices():
    print(logo)
    dices = []

    for i in range(2):
        rolling = randint(1, 6)
        dices.append(rolling)

    total = sum(dices)
    print(f"Dices: {dices}. Total: {total}")

def roll_again():
    restart = input("Press 'enter' to roll again. Otherwise, type 'exit'.\n").lower()

    if restart == "":
        print("\n" * 50)
        return True
    else:
        print("See you next time.")
        return False


def roll_it_up():
    should_continue = True
    ready = int(input("How many dices do you want to roll?\n"
                  "Type '1' or '2': "))

    if ready == 1:
        print("\n" * 50)
        while should_continue:
            one_dice()
            should_continue = roll_again()

    elif ready == 2:
        print("\n" * 50)
        while should_continue:
            two_dices()
            should_continue = roll_again()

    else:
        print("You typed an invalid option.")

roll_it_up()