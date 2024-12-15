from art import logo

vowels = ["a", "e", "i", "o", "u"]

print(logo)
print("Welcome to the Vowel Counter. Let's see how many vowels are hiding in your words.")

keep_checking = True

while keep_checking:

    vowels_to_check = input("What word or sentence would you like me to count the vowels in?\n").lower().strip()

    all_vowels = []
    non_repeated_vowels = []

    for letter in vowels_to_check:
        if letter in vowels:
            all_vowels.append(letter)

    for vowel in all_vowels:
        if vowel not in non_repeated_vowels:
            non_repeated_vowels.append(vowel)

    counted_vowels = len(non_repeated_vowels)

    print(f"'{vowels_to_check}' has {counted_vowels} vowel(s) in it: {non_repeated_vowels}")

    should_continue = input("Would you like to check another word or sentence?\n"
                            "Type 'y' for yes, or 'n' for no: ").lower().strip()

    if should_continue == "y":
        keep_checking = True
    else:
        keep_checking = False
        print("Mission complete! See you next time, vowel hunter!")