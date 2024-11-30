import random

user_choice = input('What do you choose, heads or tails?\n'
      'Type "heads" "tails".\n').lower().strip()

random_coin_toss = random.randint(0 , 1)

if random_coin_toss == 0 and user_choice == "heads":
    print("Heads. "
          "You win!")
elif random_coin_toss == 1 and user_choice == "tails":
    print("Tails. "
          "You win!")
elif random_coin_toss == 0 and user_choice == "tails":
    print("Heads. "
          "You lose.")
elif random_coin_toss == 1 and user_choice == "heads":
    print("Tails. "
          "You lose.")
else:
    print("You chose an invalid option.")