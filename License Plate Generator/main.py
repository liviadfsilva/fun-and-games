from letters_list import letters
import random

def create_plate():
    random_letters = random.sample(letters, 3)
    numbers = random.sample(range(0, 9), 4)

    letters_output = ''.join(random_letters)
    numbers_output = int(''.join(map(str, numbers)))

    plate = letters_output + str(numbers_output)

    if plate in "data.txt":
        create_plate()
    else:
        with open("data.txt", mode="a") as data:
            data.write("\n" + plate)

create_plate()
