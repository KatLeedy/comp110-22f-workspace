"""An example of conditional (if-else) statements."""

SECRET: int = 3 

print("I am thinking of a number between 1-5. What is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed corrctly!!!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess < SECRET: 
        print("Your guess is too low")
    else: 
        print("Your guess is too high")

print("Game over.")