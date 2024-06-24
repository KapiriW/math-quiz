import random

# State variables here and start math problems
mode = "regular"
questions_asked = 0
attempts = 1
guesses_allowed = 3
quiz_first = random.randint(1, 9)
quiz_second = random.randint(1, 9)
correct_answer = quiz_first + quiz_second
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

#shows instructions for the math quiz
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
# asks if user wants to read instructions
want_instructions = yes_no("Do you want to read the instructions? ")

# Checks if users want instructions
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_questions = int_check("How many questions would you like? Press <enter> for infinite mode: ")

if num_questions == "infinite":
    mode = "infinite"
    num_questions = 5  # Initial number of rounds for infinite mode

# Game loop starts here
while questions_asked < num_questions:

    # Rounds headings based on mode version
    if mode == "infinite":
        questions_heading = f"\nQuestion {questions_asked + 1} (Infinite Mode)"
    else:
        questions_heading = f"\nQuestion {questions_asked + 1} of {num_questions}"

    print(questions_heading)
    print()


    # asks the question and check if the answer is correct
    int_check(f"What is {quiz_first} + {quiz_second}? ")
    print("Good job, you got it right!")
# keeps track of how many times user gets question wrong
    questions_asked += 1


    # if users are in infinite mode increase the number of rounds
    if mode == "infinite":
        num_questions += 1

attempts_used = 0

user_response = ""
while user_response != correct_answer and attempts_used < 3:

    # ask the user to response the number...
    user_response = int_check(correct_answer)

    # check that they don't want to quit
    if user_response == "xxx":
        # set end_game to use so that outer loop can be broken
        end_game = "yes"
        break

    # add one to the number of guesses used
    attempts_used += 1

    # compare the user's response with the secret number set up feedback statement

    # If we have responses left...
    if user_response != correct_answer and attempts_used < 3:
        feedback = (f"incorrect try again remember you now only have  . "
                    f" {attempts_used} / {3} guesses")

    # when the correct number is answered, we have three different feedback
    # options (lucky / 'phew' / well done)
    elif user_response == correct_answer:

        if attempts_used == 1:
            feedback = " Lucky!  You got it on the first response. "
        elif attempts_used == correct_answer:
            feedback = f"Phew!  You got it in {attempts_used} guesses."
        else:
            feedback = f"Well done!  You guessed the secret number in {attempts_used} guesses."

        print(feedback)

        # break out of loop so user does not see 'careful' message
        # if they guessed correctly on their last response.
        break

    # if there are no guesses left!
    else:
        feedback = "Sorry - you have no more guesses.  You lose this round!"

    # print feedback to user
    print(feedback)

    # Additional Feedback (warn user that they are running out of guesses)
    if attempts_used == 3-1:
        print("\n Careful - you have one response left! \n")

# Game loop ends here
# Game History / Statistics area
print("we are done")
