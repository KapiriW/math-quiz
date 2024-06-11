# checks users enter 1,2,3,4
def q_options(question):
    while True:
        response = input(question).lower()

        # Checks user response, question
        # repeats if users don't enter a number that isn't 1,2,3,4
        if response == "1" or response == "One":
            return "1"
        elif response == "2" or response == "Two":
            return "2"
        elif response == "3" or response == "Three":
            return "3"
        elif response == "4" or response == "Four":
            return "4"
        else:
            print("please enter a number between 1 and 4")


def instruction():
    print('''


**** Instructions ****

every round there is a math question with 4 options available pick the right one you get a point if you get one wrong you dont get a point 
 try to get as high of a score as possible.

    ''')


# Checks that users enter an integer
# that is more than 13
def int_check():
    while True:
        error = "please enter a number between 1 and 4."

        try:
            response = int(input("enter an integer"))

            # checks that the number is more than 1 and no more than 4
            if response > 4:

                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine
print()
print("Math Quiz")
print()
# loop for testing


want_instructions = q_options("Do you want to read the instructions?").lower()
# checks user enter y or n
if want_instructions == "yes":
    instruction()
print()
target_score = int_check()