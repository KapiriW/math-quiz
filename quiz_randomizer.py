import random
# selects a random number from 1 and 10 twice adds them and adds them
# with the second and makes a question using the next thing
quiz_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "xxx"]

for item in range(0, 1):
    quiz_second = random.choice(quiz_list[:-1])
    quiz_first = random.choice(quiz_list[:-1])

    correct = quiz_first + quiz_second
    print(quiz_first + quiz_second)
    print(quiz_first, "+", quiz_second)





