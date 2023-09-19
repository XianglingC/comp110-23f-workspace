"""one shot wordle."""

__author__ = "730658974"

# part 1.
secret_word: str = "python"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

# part 2. Chencking indices.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Check the number of characters.
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

# Part 2.
word_idx: int = 0
emoji: str = ""
alternate_idx: int = 0
while word_idx < len(secret_word):
    if guess_word[word_idx] == secret_word[word_idx]:
        emoji += GREEN_BOX
    else:
        character_existence: bool = False
        alternate_idx = 0
# Check the guess_word's character in other places in secret_word!!!
# Don't mess up the sequence and the corresponding index for S/G.
        while not character_existence and alternate_idx < len(secret_word):
            if secret_word[alternate_idx] == guess_word[word_idx]:
                character_existence = True
            else:
                alternate_idx = alternate_idx + 1
        # If will run only when the above while is wrong.
        if character_existence is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX

    word_idx = word_idx + 1
print(emoji)
  
if guess_word != secret_word:
    print("Not quite. Play again soon!")

else:
    print("Woo! You got it!")