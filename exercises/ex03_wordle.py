""" EX03 Wordle."""

__author__ = "730658974"

#Part 4. Main_function
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    secret_word: str = "codes"
    turns: int = 1
    while turns <= 6:
        print (f"===Turn {turns}/6 ===")
        user_guess: str = input_guess(len(secret_word))
        emoji_result: str = emojified(user_guess, secret_word)
        print(emoji_result)

        if user_guess == secret_word:
            response: str = print(f"You won in {turns}/6 turns!")
            return response 
        #something must change in the while loop
        turns += 1
    if turns == 7:
        response: str = print (f"X/6 - Sorry, try again tomorrow!") 
        return response

# Part 1. Based on EX02 define the function
def contains_char(string1: str, single_charactor: str) -> bool:
    """define the function that has 2 parameters for the checking process"""
    alternate_idx: int = 0
    character_existence: bool = False
    assert len(single_charactor) == 1
    while not character_existence and alternate_idx < len(string1):
        if string1[alternate_idx] == single_charactor:
            character_existence = True
        else:
            alternate_idx += 1
    if character_existence is True:
        return True
    else:
        return False

# Part 2. emojified
def emojified(guess: str, secret: str) -> str:
    """Checking the character and apply emoji"""
    assert len(guess) == len(secret)
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    word_idx: int = 0
    while word_idx < len(secret):
        if guess[word_idx] == secret[word_idx]:
            emoji += GREEN_BOX
            #Calling the function
        else:
            character_in_word: bool = contains_char(secret, guess[word_idx])
            if character_in_word is True:
                emoji += YELLOW_BOX   
            else:
                emoji += WHITE_BOX
        word_idx += 1  
    return emoji

#Part 3. input_guess
def input_guess(expected_length: int) -> str:
    #prompt the user finding the correct length
    user_input: str = input(f"Enter a {expected_length} character word: ")
    while len(user_input) != expected_length:
        user_input = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_input
 
if __name__ == "__main__":
    main()