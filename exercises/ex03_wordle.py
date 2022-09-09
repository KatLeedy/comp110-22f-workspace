"""A structured Wordle game."""
__author__: str = "730610012"

secret: str = "codes"

def contains_char(goal_word: str, current_letter: str) -> bool:
    """Checks if a given character is found anywhere in a given string."""
    assert len(current_letter) == 1
    in_word: bool = False
    i: int = 0
    while i < len(goal_word):
        if goal_word[i] == current_letter:
            in_word = True
        i += 1
    return in_word

def emojified(sec: str, guess: str) -> str: 
    """Takes a user's guess and returns an emoji representation."""
    #Green box means right letter, right place
    #Yellow box means letter is in secret word, but not in the current index
    #White box means letter is not in secret word
    assert len(guess) == len(sec)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_rep: str = ""
    j: int = 0
    while j < len(guess):
        if guess[j] == sec[j]: 
            emoji_rep += GREEN_BOX
        elif contains_char(sec, guess[j]):
            emoji_rep += YELLOW_BOX
        else: 
            emoji_rep += WHITE_BOX
        j += 1
    return emoji_rep

def input_guess(expected_len) -> str: 
    """Checks that user inputs guess of the correct length and returns that guess."""
    user_input: str = input("Enter a 5 character word: ")
    while len(user_input) != expected_len:
        user_input = input("That wasn't 5 chars! Try again: ")
    return user_input

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns_played: int = 1
    won: bool = False
    while turns_played <= 6 and not won: 
        print(f"=== Turn {turns_played}/6 ===")
        player_guess: str = input_guess(len(secret)) 
        #checks that guess is correct length
        player_guess = emojified(secret, player_guess)
        #turns guess into emoji representation
        print(player_guess)
        if player_guess == "\U0001F7E9" * len(player_guess):
            won = True
        else:
            turns_played +=1
    if won: 
        print(f"You won in {turns_played}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")
    
if __name__ == "__main__":
    main()


