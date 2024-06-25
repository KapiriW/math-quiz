import random

# State variables here and show attempts allocated/allowed
mode = "regular"
questions_asked = 0
attempts = 1
attempts_allowed = 3

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

# Shows instructions for the math quiz
def instruction():
    print('''
**** Instructions ****
Welcome to my math quiz. This quiz will cover basic addition.
Try not to slip up and pick the number of questions or 
press enter for infinite mode.
    ''')

# Integer checker function for question count input
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

# Main routine
print()
print("Math Quiz")
print()

print("Welcome to the math quiz")
print()
# Asks if user wants to read instructions
want_instructions = yes_no("Do you want to read the instructions? ")

# if yes show instruction if no skip instructions
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_questions = int_check("How many questions would you like? Press <enter> for infinite mode: ")

if num_questions == "infinite":
    mode = "infinite"
    num_questions = 5  # Infinite mode set to a very large number

# Game loop starts here
while questions_asked < num_questions:
    # Round headings based on mode version
    if mode == "infinite":
        questions_heading = f"\nQuestion {questions_asked + 1} (Infinite Mode)"
    else:
        questions_heading = f"\nQuestion {questions_asked + 1} of {num_questions}"

    print(questions_heading)
    print()

    # Makes and asks the question and check if the answer is correct
    quiz_first = random.randint(1, 9)
    quiz_second = random.randint(1, 9)
    correct_answer = quiz_first + quiz_second

    attempts_used = 0
    user_response = None

    while user_response != correct_answer and attempts_used < attempts_allowed:
        # Ask the user to respond to the question
        user_response = input(f"What is {quiz_first} + {quiz_second}? ")
        if user_response.lower() == "xxx":
            end_game = "yes"
            break

        try:
            user_response = int(user_response)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Add one to the number of guesses used
        attempts_used += 1

        if mode == "infinite":
            num_questions += 1

        # Compare the user's response with the correct answer
        if user_response != correct_answer:
            if attempts_used < attempts_allowed:
                feedback = f"Incorrect. Try again. You have {attempts_allowed - attempts_used} guesses left."
            else:
                feedback = "Sorry - you have no more guesses. You lose this round!"
        else:
            feedback = f"Phew! You got it in {attempts_used} guesses."

        # Print feedback to user
        print(feedback)

        # Warn user that they are running out of guesses
        if attempts_used == attempts_allowed - 1 and user_response != correct_answer:
            print("\nCareful - you have one response left!\n")

    questions_asked += 1

    # If in infinite mode and user chose to end game
    if mode == "infinite" and 'end_game' in locals():
        break

# Game loop ends here
print("We are done")
