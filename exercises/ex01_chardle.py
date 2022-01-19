"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730464051"

word: str = input("Enter a 5-character word: ")
occurrences = 0

if len(word) == 5:
    letter: str = input("Enter a single character: ")
    print("Searching for " + letter + " found in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        occurrences = occurrences + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        occurrences = occurrences + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        occurrences = occurrences + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        occurrences = occurrences + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        occurrences = occurrences + 1
    if occurrences == 0:
        print("No occurrences of " + letter + " found in " + word)
    else:
        if occurrences == 1:
            print(str(occurrences) + " instance of " + letter + " found in " + word)
        else: 
            print(str(occurrences) + " instances of " + letter + " found in " + word)
else:
    print("Error: Word must contain 5 characters")