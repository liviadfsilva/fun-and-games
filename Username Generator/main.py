import random

adjectives = ["cutie", "macabre", "amazing", "little", "hot", "incredible", "unbelievable", "marvelous", "maleficent"]
mythical_things = ["fae", "pegasus", "basilisk", "vampire", "werewolf", "zombie", "fairy", "siren"]

print("Welcome to the Username Generator")
user_choice = int(input("How many random usernames would you like to generate? "))

for choice in range(user_choice):
    adj = random.choice(adjectives)
    myth = random.choice(mythical_things)
    number = random.randint(0, 99)

    username = adj + myth + str(number)

    print(f"Your username {choice + 1} is: {username}")