from art import cute_art

words = []

print(f"Welcome to the {cute_art}")
checker = input("Make sure your text doesn't contain commas(,), periods(.), semi-colons(:) or colons(:) \n"
                "Insert your text here to have the repeated words: "). lower()

if checker !="":
    each_word = checker.split()

    for i in each_word:
        if i not in words:
            words.append(i)

print (words)