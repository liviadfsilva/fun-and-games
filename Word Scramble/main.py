import random
from scramble_art import logo
from scramble_words import easy, medium, hard

print(logo)

lives = 6

words_list = [easy, medium, hard]

print("Welcome to Word Scramble!")
difficulty_level = input('Choose a difficulty level:\n'
                         'Type "easy", "medium" or "hard".\n').lower().strip()

if difficulty_level == "easy":
    words_list = easy
elif difficulty_level == "medium":
    words_list = medium
elif difficulty_level == "hard":
    words_list = hard
else:
    print("You chose an invalid option.")
    words_list = None

if words_list:
    original_word = random.choice(words_list)
    scrambled_word = list(original_word)
    random.shuffle(scrambled_word)
    final_word = ''.join(scrambled_word)

    print(final_word)
    correct_word = original_word

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