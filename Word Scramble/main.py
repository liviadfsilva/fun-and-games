import random
from scramble_art import logo
from scramble_words import easy, medium, hard

print(logo)

lives = 6

original_easy_word = random.choice(easy)
original_medium_word = random.choice(medium)
original_hard_word = random.choice(hard)

print("Welcome to Word Scramble!")
difficulty_level = input('Choose a difficulty level:\n'
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

game_over = False

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("What word is that?\n")

    if guess != correct_word:
        lives -= 1
        print(f"You guessed {guess}. That's not the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {correct_word}! YOU LOSE**********************")


    if guess == correct_word:
        game_over = True
        print("****************************YOU WIN****************************\n"
            f"The right word is: {correct_word} from the {difficulty_level} level!")