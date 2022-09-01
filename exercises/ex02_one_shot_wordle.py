"""Another step towards a Wordle game."""
__author__ = "730610012"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"

user_guess: str = input(f"What is your {len(secret)}-letter guess?")
while len(user_guess) != len(secret):
    user_guess = input("That was not 6 letters! Try again:")

i: int = 0
color_result: str = ""

while i < len(secret):
    letter_in_secret: bool = False
    j: int = 0
    while j < len(secret):
        if user_guess[i] == secret[j]:
            letter_in_secret = True
        j += 1
    
    if user_guess[i] == secret[i]:
        color_result += GREEN_BOX
    elif letter_in_secret:
        color_result += YELLOW_BOX
    else:
        color_result += WHITE_BOX
    i += 1

print(color_result)

if color_result == GREEN_BOX * len(secret):
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")