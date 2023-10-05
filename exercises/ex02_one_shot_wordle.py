"""Creating a One Shot Wordle."""

__author__ = "730556575"

# setting up variables 
secret_word: str = "python"
guess: str = input(f"What is your { len(secret_word) }-letter guess? ")
new_guess: str = ""
# boxes variable
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# checking each index
index: int = 0
boxcolor: str = ""

# loop for guesses 
while len(guess) != 6:
    new_guess = input(f"That was not { len(secret_word)} letters! Try again: ")
    guess = new_guess

# checking index in correct places 
# loop to see whether there are matching words within the code, and if so make yellow
while index < len(secret_word): 
    if guess[index] == secret_word[index]: 
        boxcolor += GREEN_BOX
    else: 
        in_word: bool = False
        alt_index: int = 0
        while in_word is False and alt_index < len(secret_word):
            if guess[index] == secret_word[alt_index]:
                in_word = True
            else: 
                alt_index = alt_index + 1
        if in_word: 
            boxcolor += YELLOW_BOX
        else: 
            boxcolor += WHITE_BOX
    index = index + 1
print(boxcolor)

# after the boxcolor
if (guess != secret_word): 
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")