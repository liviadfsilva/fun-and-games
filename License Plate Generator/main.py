from letters_list import letters
import random

def create_plate():
    all_plates = []
    random_letters = random.sample(letters, 3)
    numbers = random.sample(range(0, 9), 4)

    letters_output = ''.join(random_letters)
    numbers_output = int(''.join(map(str, numbers)))

    plate = letters_output + str(numbers_output)

    with open("data.txt", mode="r") as data:
        existing_plates = data.read().splitlines()

    if plate not in existing_plates:
        with open("data.txt", mode="a") as data:
            data.write("\n" + plate)
            all_plates.append(plate)
    else:
        print("Plate already exists.")


create_plate()