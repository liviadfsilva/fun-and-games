from lists import cap_letters, plates
import random

generator_is_on = True

def generate_plate():
    letters = random.choices(cap_letters, k=3)
    numbers = random.choices(range(0, 9), k=4)

    let_result = ''.join(letters)
    nr_result = ''.join(map(str, numbers))

    license_plate = let_result + nr_result
    if license_plate in plates:
        generate_plate()
    else:
        plates.append(license_plate)
        print(f"Your license plate is: {license_plate}")

while generator_is_on:
    ask_user = input("Would you like to generate a license plate? (Y/N)\n").lower().strip()

    if ask_user == "y":
        generate_plate()
    else:
        generator_is_on = False