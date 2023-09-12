"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730556575"
 
# inputs and variables 
five_character_word: str = input("Enter a 5 word character: ")
if len(five_character_word) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + (character) + " in " + (five_character_word))

if five_character_word[0] == character:
    print((character) + " found at index 0")
if five_character_word[1] == character:
    print((character) + " found at index 1")
if five_character_word[2] == character:
    print((character) + " found at index 2")
if five_character_word[3] == character:
    print((character) + " found at index 3")
if five_character_word[4] == character:
    print((character) + " found at index 4")

indices_counter: int = 0
if five_character_word[0] == character:
    indices_counter = indices_counter + 1
if five_character_word[1] == character:
    indices_counter = indices_counter + 1
if five_character_word[2] == character:
    indices_counter = indices_counter + 1
if five_character_word[3] == character:
    indices_counter = indices_counter + 1
if five_character_word[4] == character:
    indices_counter = indices_counter + 1

if indices_counter == 1: 
    print(str(indices_counter) + " instance of " + (character) + " found in " + (five_character_word))
if indices_counter > 1: 
    print(str(indices_counter) + " instances of " + (character) + " found in " + (five_character_word))
if indices_counter == 0: 
    print("No instances of " + (character) + " found in " + (five_character_word))