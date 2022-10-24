"""A fun little day in the life of a small UNC freshman."""

__author__ = "730610012"


from random import randint

# Player starts with 3 overall points. A player loses a 
# point when any of their other point categories go below 0.  
points: int
player: str
health_points: int
energy_points: int
knowledge_points: int
social_points: int

BLUE_SHIRT_EMOJI: str = "\U0001F455"
MUSCLE_EMOJI: str = "\U0001F4AA"
SUN_EMOJI: str = "\U0001F31E"
SPARKLE_EMOJI: str = "\U00002728"
TIRED_EMOJI: str = "\U0001F4A4"
DASHED_LINE_EMOJI: str = "\U0000FAE5"
BRAIN_EMOJI: str = "\U0001F9E0"
FOOD_BOWL_EMOJI: str = "\U0001F35B"
SALAD_EMOJI: str = "\U0001F957"


def greet() -> None:
    """Greets the player, explains the game, and assigns the global player variable to the user's input."""
    global player
    print("WELCOME TO THE LIFE OF A UNC STUDENT. YOU WILL NAVIGATE A DAY AS A COLLEGE STUDENT MAKING CHOICES THAT CAUSE YOU TO GAIN AND LOSE HEALTH, KNOWLEDGE, SOCIAL, ENERGY, AND OVERALL POINTS. WHEN ANY SUB-CATEGORY OF POINTS REACHES 0 OR BELOW, YOU LOSE ONE OVERALL POINT. ALTERNATELY, WHEN ANY CATEGORY OF SUBPOINTS REACHES 1O OR ABOVE, YOU GAIN ONE OVERALL POINT. ENJOY!")
    player = input("Enter your name: ")
    print(f"Hi {player}, good luck!")
    print(" (•◡•) /")


def set_subpoints(x: str) -> None:
    """Based on the user's choice passed to the function, sets the initial subpoints."""
    global health_points, energy_points, knowledge_points, social_points
    if x == "a":
        health_points = 5
        print("\nYou start with 5 health points.")
        energy_points = 5
        print("You start with 5 energy points. Enjoy the extra energy from your short walk.")
        knowledge_points = 7
        print("You start with 7 knowledge points. The creator of this program is impressed with your physics knowledge.")
        social_points = 3
        print("You start with 3 social points. North campus is a little too quiet.")
    elif x == "b":
        health_points = 7
        print("\nYou start with 7 health points. You are pre-med and \"just really into lifting right now\"")
        energy_points = 3
        print("You start with 3 energy points. The 20 min walk to your 8am has you a little sluggish.")
        knowledge_points = 5
        print("You start with 5 knowledge points.")
        social_points = 5
        print("You start with 5 social points. Your suite is a delight.")
    else:
        health_points = 3
        print("\nYou start with 3 health points. You may have mild mold poisoning.")
        energy_points = 5
        print("You start with 5 energy points.")
        knowledge_points = 5
        print("You start with 5 knowledge points.")
        social_points = 7
        print("You start with 7 social points. You are likely in greek life if we're being honest.")


def change_health_points(change_hth: int) -> None:
    """Changes the health subpoint global variable by a specific number. Changes global points if less than 0 or more than 10."""
    global health_points, points
    health_points += change_hth
    if change_hth > 0:
        print(f"Wow, that was a good choice for your health! +{change_hth} health points")
    else:
        print(f"Hmmm :l your health took a hit. {change_hth} health points") 
    if health_points < 1:
        points += -1
    if health_points > 9:
        points += 1


def change_energy_points(change_en: int) -> None:
    """Changes the energy subpoint global variable by a specific number. Changes global points if less than 0 or more than 10."""
    global energy_points, points
    energy_points += change_en
    if change_en > 0:
        print(f"ZAP. You are suddenly brimming with energy {SPARKLE_EMOJI} +{change_en} energy points")
    else:
        print(f"...you...are...feeling a little tired {TIRED_EMOJI} {change_en} energy points")
    if energy_points < 1:
        points += -1
    if energy_points > 9:
        points += 1


def change_knowledge_points(change_know: int) -> None:
    """Changes the knowledge subpoint global variable by a specific number. Changes global points if less than 0 or more than 10."""
    global knowledge_points, points
    knowledge_points += change_know
    if change_know > 0:
        print(f"Learning is truly incredible. You are gaining knowledge at a remarkable pace. {BRAIN_EMOJI} +{change_know} knowledge points")
    else:
        print(f"Uhhhhhh, your brain is atrophying {change_know} knowledge points")
    if knowledge_points < 1:
        points += -1
    if knowledge_points > 9:
        points += 1


def change_social_points(change_soc: int) -> None:
    """Changes the social subpoint global variable by a specific number. Changes global points if less than 0 or more than 10."""
    global social_points, points
    social_points += change_soc
    if change_soc > 0:
        print(f"You are quite the social butterfly. They love you! You could start your own cult soon :D +{change_soc} social points")
    else:
        print(f"As you recede into the background, you fear no one will remember you. That or you are being annoying :l {DASHED_LINE_EMOJI} {change_soc} social points")
    if social_points < 1:
        points += -1
    if social_points > 9:
        points += 1


def print_all_points() -> None:
    """Prints the value of each category of global subpoints and overall points."""
    print("\n")
    print(f"\npoints: {points}")
    print(f"health_points: {health_points}")
    print(f"energy_points: {energy_points}")
    print(f"knowledge_points: {knowledge_points}")
    print(f"social_points: {social_points}")
    print("\n")


def check_input_abc(user_input: str) -> str:
    """Checks that the input is "a", "b", or "c"."""
    while (user_input != "a") and (user_input != "b") and (user_input != "c"):
        user_input = input("Please enter a valid input: ")
    return user_input


def check_input_yn(user_input: str) -> str:
    """Checks that the input is "y" or "n"."""
    while (user_input != "y") and (user_input != "n"):
        user_input = input("Please enter a valid input: ")
    return user_input


# Contains use of random() 
def lead_poisoning() -> None:
    """Randomly generates an integer that determines whether user received lead poisoning, which updates global health subpoints."""
    concentration: int = randint(1, 10)
    if concentration <= 3:
        print("Whew! Your water did not contain lead, and your health was unaffected :)")
    elif concentration <= 7:
        print("Oh no! The water you drank contained trace amounts of lead. Oops, so silly of the university.")
        change_health_points(-2)
    else:
        print("EEK! That water had a LOT of lead. Is your head feeling cloudy?")
        change_health_points(-4)


# This function should satisfy category 4 on the write-up.
def office_hours(x: int) -> int:
    """Changes the user's global points variable based on their input regarding attending office hours."""
    go_to_sitterson: str = check_input_yn(input("You're having a little trouble with your COMP110 exercise! Do you attend office hours? Enter y or n: "))
    if go_to_sitterson == "y":
        print("You log onto coursecare and see \"Hi, {player}. There are three students queued.\" After a short wait, you enter the room to be helped.")
        print("Wow. Because office hours are so very valuable, you gain one overall point!")
        return x + 1
    else:
        print("Ah, your loss. You won't get the life-changing experience that is COMP110 office hours :( In fact, you missed out so much that you lose one overall point.")
        return x - 1


# This function should satisfy category 3 on the write-up.
def save_child() -> None:
    """Changes the user's global points variable based on their input regarding saving a child."""
    global points
    moral_decision: str = check_input_yn(input("As you're walking from the library, you see AHHHH A CHILD IS RUNNING INTO THE STREET. Do you grab the child and save them from the oncoming traffic?\nEnter y or n:\n"))
    if moral_decision == "y":
        print(f"Whew. That was close! {player}, for your good deed, you gain one overall point!")
        points += 1
    else:
        print(f"....>-|0...... The child could've been seriously hurt! You are not a good person, {player}. -_- For this callous decision, you lose one overall point.")
        points += -1


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    global points, player, health_points, energy_points, knowledge_points, social_points
    points = 3
    greet()
    play_again: bool = True
    while play_again:
        # Players choose a starting role with varying initial subpoints
        print("Before beginning your college journey, you must make a decision!\nAre you:\nA) An Astronomy major living in Stacy hall\nB) A Biology major living in Hinton James hall\nC) A Communications major living in Granville Towers")
        life_choice: str = check_input_abc(input("Please enter a, b, or c to continue: "))
        set_subpoints(life_choice)

        # Choose whether to go to class
        class_decision: str = check_input_abc(input(f"\n{SUN_EMOJI} GOOOOOD MORNING! It's time for class but it's oh so early. Do you:\na) Go to class! I am here to learn.\nb) Skip class. The extra sleep is worth it.\nC) Go to the gym. It's never the wrong time to work out.\nEnter a, b, or c: "))
        print("\n")
        if class_decision == "a":
            print("You decide to drag yourself out of bed and go to lecture. So academic")
            change_knowledge_points(2)
            change_energy_points(-1)
        elif class_decision == "b":
            print("You turn off your alarm and drift into blissful sleep without giving class another thought.\n(- _ -) zzz")
            change_knowledge_points(-2)
            change_energy_points(2)
        else:
            print(f"You get a great lifting session in. So strong {MUSCLE_EMOJI}")
            change_knowledge_points(-2)
            change_health_points(1)
        print_all_points()

        # Choose a drink
        where_drink: str = check_input_abc(input("\nYou're feeling a little thirsty! Do you:\nA) Get a quick sip from the refreshing water fountain.\nB) Walk to the Campus Y to get a fun little drink.\nC) I'm too good for fluids.\nEnter a, b, or c: "))
        if where_drink == "a":
            print("THIS JUST IN: UNC has recently discovered lead in several water fixtures across campus.\nHave you consumed heavy metal?\n...")
            lead_poisoning()
        elif where_drink == "b":
            print("Mmmm, an iced mocha. So so tasty.")
            change_energy_points(1)
        else:
            print("You make the questionable decision to not get a drink. A slight headache sets in.")
            change_health_points(-2)
        print_all_points()
        
        # Choose an activity on the quad
        quad_decision: str = check_input_abc(input("As you walk through the quad, you see a lot of activity. Do you:\nA) Go pet a dog! So sweet and cute.\nB) Join a club. You have some extra time.\nC) Stop by the student stores to pick up some fun merch.\nEnter a, b, or c: "))
        if quad_decision == "a":
            print("woof\n૮ ・ﻌ・ა")
            change_health_points(1)
        elif quad_decision == "b":
            print("You sign up for a book club--yay reading!")
            change_knowledge_points(2)
            change_social_points(1)
        else:
            print(f"You decide to do a little shopping. You pick out a snazzy UNC shirt.\n{BLUE_SHIRT_EMOJI}")
        print_all_points()

        # Choose a library activity
        lib_activity_choice: str = check_input_abc(input("You find a seat in the reading room of Davis. Do you:\nA) Watch TikTok.\nB) Study, even if I haven't talked to a human all day! I'm an absolute academic weapon.\nC)Talk loudly to your friend on the silent floor.\nEnter a, b, or c: "))
        if lib_activity_choice == "a":
            print("You ignore your 12 assignments and scroll on your phone.")
            change_knowledge_points(-1)
            change_health_points(-1)
        elif lib_activity_choice == "b":
            print("You may not have friends, but you're going to have an A in CHEM101.")
            change_knowledge_points(1)
            change_social_points(-1)
        else:
            print("Your peers are not a fan of your overly public conversation.")
            change_social_points(-2)
        print_all_points()

        # Choose whether or not to save a child.
        save_child()
        print_all_points()

        # Choose a meal
        meal_choice: str = check_input_abc(input("Ooooh you're getting hungry. Do you:\nA) Grab some chicken stir fry, salad, and a brownie.\nB) Eat two pieces of cheesecake for dinner.\nC) Ignore your rumbling stomach.\nEnter a, b, or c: "))
        if meal_choice == "a":
            print(f"A balanced meal! {SALAD_EMOJI} {FOOD_BOWL_EMOJI}")
            change_health_points(2)
            change_energy_points(1)
        elif meal_choice == "b":
            print("Maybe a questionable choice for dinner, but that's all right.")
            change_health_points(-1)
            change_energy_points(1)
        else:
            print("You've gotta eat!!")
            change_health_points(-2)
            change_energy_points(-3)
        print_all_points()

        # Visit Comp110 office hours.
        points = office_hours(points)
        print_all_points()

        # Choose an evening activity
        evening_activity: str = check_input_abc(input("It's nearing the end of the day, and it's time to choose an activity for the evening. Do you:\nA) Relax! Watch Netflix--you enjoy a little time to chill out.\nB) Late night at Davis. Again. The Safewalk people know me by name now.\nC) Call a friend! It's been a long time since you've talked.\nEnter a, b, or c: "))
        if evening_activity == "a":
            print("Very nice way to wind down for the night.")
            change_energy_points(2)
        elif evening_activity == "b":
            print("You show admirable dedication to your classwork.")
            change_knowledge_points(2)
            change_energy_points(-2)
        else:
            print("So nice to catch up!")
            change_energy_points(1)
            change_social_points(2)
        print_all_points()
        
        # End of day
        print("Ahhhh, you've finally reached the end of your day! It's time to lay down on your tiny matress and drift off into a sleep completely unbroken by random fire alarms and slamming doors.\n(◕ ‿ ◕)\n(- ‿ -)\n(- _ -) zzz")
        play_again_answer: str = check_input_yn(input("Would you like to play again? If you play again, you may choose a different starting role (your health, social, knowledge, and energy points will reset) but retain the same number of overall \"points.\"\nEnter y or n: "))
        if play_again_answer == "n":
            play_again = False
        else:
            print(f"\nYour have {points} overall points.\n")
    print("\nYour final points were:")
    print_all_points()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()