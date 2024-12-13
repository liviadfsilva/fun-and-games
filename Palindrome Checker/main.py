import art

print(art.logo)
print("Welcome to the Ultimate Palindrome Checker")
print("Is your word or phrase a palindrome? Let's find out!")

keep_checking = True

while keep_checking:

    input_to_check = input("Enter a word or phrase below to check:\n").lower().strip()

    if input_to_check.isdigit():
        print("You entered an invalid input. Please enter a word or phrase, not a number.")
    else:
        input_to_check = input_to_check.lower().strip()

        def reverse_input(x):
            return x[::-1]

        reversed_string = reverse_input(input_to_check)

        if reversed_string == input_to_check:
            print(f"{reversed_string} is a palindrome, for it reads the same backward as forward.")
        elif reversed_string == int:
            print("You typed an invalid input.")
        else:
            print(f"{reversed_string} is NOT a palindrome, for it doesn't read the same as {input_to_check}.")

        should_continue = input("Would you like to check another word or phrase?\n"
                                "Type 'y' for yes, or 'n' for no. ")

        if should_continue == "y":
            keep_checking = True
        else:
            keep_checking = False