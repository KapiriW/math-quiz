import random

# State variables here
mode = "regular"
rounds_played = 0

# Ensures that instructions can be read or not read
def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instruction():
    print('''


**** Instructions ****
Welcome to my math quiz. This quiz will cover basic addition.
Try not to slip up and pick the number of rounds or 
press enter for infinite mode.
    ''')


# Integer checker function for round input
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more, or press Enter for infinite mode."

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Integer checker function for quiz answers
# i made an additional integer checker so that i can answer the question
def int_checker1(question, correct_answer):
    while True:
        error = "You got the answer wrong. Try again."

        try:
            response = int(input(question))

            # Checks if the answer is correct
            if response == correct_answer:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
print()
print("Math Quiz")
print()

print("Welcome to the math quiz")
print()
# asks if user wants to read instructions
want_instructions = yes_no("Do you want to read the instructions? ")

# Checks if users want instructions
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5  # Initial number of rounds for infinite mode

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nRound {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    # Generate a math question
    quiz_first = random.randint(1, 10)
    quiz_second = random.randint(1, 10)
    correct_answer = quiz_first + quiz_second

    # asks the question and check if the answer is correct
    int_checker1(f"What is {quiz_first} + {quiz_second}? ", correct_answer)
    print("Good job, you got it right!")

    rounds_played += 1

    # if users are in infinite mode increase the number of rounds
    if mode == "infinite":
        num_rounds += 1

print("\nThank you for playing the math quiz!")
