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
welcome to my maths quiz this quiz will cover basic addition try not to slip up and pick the amount of rounds or 
press enter for infinite modeWIP
    ''')


# Main routine
print()
print("Math Quiz")
print()
# loop for testing


#want_instructions = yes_no("Do you want to read the instructions?").lower()
# checks user enter y or n
# if want_instructions == "yes":
 #   instruction()
#print("")
#start = yes_no("would you like to start now? ill change this to questions / inf mode later").lower()


# Game loop ends here

# Game History / Statistics area

#this integer checker works for the quiz answers
#def int_checker1(question):
 #   while True:
  #      error = "you got the answer wrong try again ."

   #     try:
    #        response = int(input(question))

     #       # checks that the number is more than / equal to 13
      #      if response == quiz_first + quiz_second:
       #         return response
        #    else:
         #       print(error)

        #except ValueError:
         #   print(error)
            #this int check handles the inf mode

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)
# selects a random number from 1 and 10 twice adds them and adds them
# with the second and makes a question using the next thing


mode = "regular"
rounds_played = 0

print(" welcome to the math quiz ")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

quiz_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "xxx"]
for item in range(0, 1):
    quiz_second = random.choice(quiz_list[:-1])
    quiz_first = random.choice(quiz_list[:-1])
# asks a question and checks if the answer typed is correct wip
    correct = int_check(f"what is {quiz_first} + {quiz_second} = ???".lower())
   # query = "what is the answer"
    print("good job you got it right")
