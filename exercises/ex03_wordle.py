"""Making a Structured Wordle."""

__author__ = "730556575"


# to see if character is within the word
def contains_char(secret_word: str, single_character: str) -> bool: 
    """Searching for character within the word."""
    assert len(single_character) == 1
    index: int = 0 
    while index < len(secret_word): 
        if single_character == secret_word[index]: 
            return True
        else: 
            index = index + 1
    return False


def emojified(guess: str, secret_word: str) -> str: 
    """Seeing if characters within the word is in the right place or not."""
    index: int = 0 
    boxcolor: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret_word)
    while index < len(guess): 
        if secret_word[index] == guess[index]: 
            boxcolor += GREEN_BOX
        elif contains_char(secret_word, guess[index]) is True:  # if the secret word character does not equal the guess index but is still in word
            boxcolor += YELLOW_BOX
        else:  # if the character is not even in the word at all
            boxcolor += WHITE_BOX
        index = index + 1
    return boxcolor


def input_guess(length: int) -> str: 
    """See if the length is correct."""
    guess = input(f"Enter a { length} character word: ")
    new_guess: str = ""
    while len(guess) != length: 
        new_guess = input(f"That wasn't { length} chars! Try again: ")
        guess = new_guess
    return guess


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    # number of max number of tries 
    max: int = 6 
    turn: int = 1 
    secret_word: str = "codes"
    game_status: bool = False
    # prompt user for a guess 
    while turn <= max and game_status is False: 
        print(f"=== Turn { turn}/{ max} ===")
        guess: str = input_guess(len(secret_word))
        # print out the emojified function
        boxcolor = emojified(guess, secret_word)
        print(boxcolor)
        # if it is the correct guess
        if secret_word == guess: 
            print(f"You won in { turn}/{ max} turns!")
            game_status = True
        else:  # keeps on giving tries till 6
            turn = turn + 1
    if game_status is False: 
        print(f"X/{ max} - Sorry, try again tomorrow!")


if __name__ == "__main__": 
    main()