"""EX01 - Chardle - A cute step toward Wordle"""
__author__ = "730610012"

user_word: str = input("Enter a 5-character word: ")
user_character: str = input("Enter a single character: ")
print("Searching for " + user_character + "in " + user_word)

if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(user_character) != 1:
    print(Error: Character must be a single character.)
    exit()

count: int = 0
if user_word[0] == user_character: 
    count = count + 1 
    print(user_character + " is found at index 0")
if user_word[1] == user_character: 
    count = count + 1 
    print(user_character + " is found at index 1")
if user_word[2] == user_character: 
    count = count + 1 
    print(user_character + " is found at index 2")
if user_word[3] == user_character: 
    count = count + 1 
    print(user_character + " is found at index 3")
if user_word[4] == user_character: 
    count = count + 1 
    print(user_character + " is found at index 4")
else: 
    print("No instances of " + user_character + " found in " + user_word)

