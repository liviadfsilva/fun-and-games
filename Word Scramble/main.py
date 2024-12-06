import random
from scramble_art import logo
from scramble_words import easy, medium, hard

print(logo)

original_easy_word = random.choice(easy)
original_medium_word = random.choice(medium)
original_hard_word = random.choice(hard)

difficulty_level = input('Welcome to Word Scramble!\n'
                         'Choose a level of difficulty:'
                         'Type "easy", "medium" or "hard".\n').lower().strip()

if difficulty_level == "easy":
    easy_word = list(original_easy_word)
    random.shuffle(easy_word)
    final_easy_word = ''.join(easy_word)
    print(final_easy_word)
    correct_word = original_easy_word
elif difficulty_level == "medium":
    medium_word = list(original_medium_word)
    random.shuffle(medium_word)
    final_medium_word = ''.join(medium_word)
    print(final_medium_word)
    correct_word = original_medium_word
elif difficulty_level == "hard":
    hard_word = list(original_hard_word)
    random.shuffle(hard_word)
    final_hard_word = ''.join(hard_word)
    print(final_hard_word)
    correct_word = original_hard_word
else:
    print("You chose an invalid option.")
    correct_word = None

guess = ""

while guess != correct_word:
    guess = input("What word is that?\n")

    if guess == correct_word:
        print(f"You did it! That's the right word: {guess} from the {difficulty_level} level!")
    else:
        print("Wrong answer. Try again.")