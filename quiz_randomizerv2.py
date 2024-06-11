import random
# state variables here

# ensures that instructions can be read or not read
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
WIP
    ''')


# Main routine
print()
print("Math Quiz")
print()
# loop for testing


want_instructions = yes_no("Do you want to read the instructions?").lower()
# checks user enter y or n
if want_instructions == "yes":
    instruction()
print("")
start = yes_no("would you like to start now?").lower()

# selects a random number from 1 and 10 twice adds them and adds them
# with the second and makes a question using the next thing
quiz_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "xxx"]

for item in range(0, 1):
    quiz_second = random.choice(quiz_list[:-1])
    quiz_first = random.choice(quiz_list[:-1])
# asks a question and checks if the answer typed is correct wip
    correct = (quiz_first + quiz_second)
   # query = "what is the answer"
    print(quiz_first, "+", quiz_second, "= ???")
