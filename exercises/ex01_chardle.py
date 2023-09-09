"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730658974"

# Part 1.
user_input_word: str = input("Enter a 5-character word: ")

if len(user_input_word) == 5:
    single_character: str = input("Enter a single character: ")
else:
    print("Error: Word must contain 5 characters")
    exit()

if len(single_character) == 1:
    print("Searching for " + single_character + " in " + user_input_word)
else:
    print("Error: Character must be a single character.")
    exit()

# Part 2 + Part 3
number_of_matching_characters: int = 0

if single_character == user_input_word[0]:
    print(single_character + " found at index" + " 0")
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == user_input_word[1]:
    print(single_character + " found at index" + " 1") 
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == user_input_word[2]:
    print(single_character + " found at index" + " 2")
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == user_input_word[3]:
    print(single_character + " found at index" + " 3")
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == user_input_word[4]:
    print(single_character + " found at index" + " 4")
    number_of_matching_characters = number_of_matching_characters + 1

# part 3
if number_of_matching_characters == 1:
    print(str(number_of_matching_characters) + " instance of " + single_character + " found in " + user_input_word)

if number_of_matching_characters == 2:
    print(str(number_of_matching_characters) + " instances of " + single_character + " found in " + user_input_word)

if number_of_matching_characters == 3:
    print(str(number_of_matching_characters) + " instances of " + single_character + " found in " + user_input_word)

if number_of_matching_characters == 4:
    print(str(number_of_matching_characters) + " instances of " + single_character + " found in " + user_input_word)

if number_of_matching_characters == 5:
    print(str(number_of_matching_characters) + " instances of " + single_character + " found in " + user_input_word)

if number_of_matching_characters == 0:
    print("No instances of " + single_character + " found in " + user_input_word)