import random

run = True
while run:
    print("Please enter the number from 1 to 3 to choose one of this options")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user = int(input())

    print("Your choice is: ", end="")
    if (user == 1):
        print("Rock")
    elif (user == 2):
        print("Paper")
    else:
        print("Scissors")

    print("Now its computer turn...")
    computer = random.randint(1, 3)

    print("Computer's choice is: ", end="")
    if (computer == 1):
        print("Rock")
    elif (computer == 2):
        print("Paper")
    else:
        print("Scissors")

    if (user == computer):
        print("Draw!")
    elif (user == 1 and computer == 3):
        print("You win!")
    elif (user == 2 and computer == 1):
        print("You win!")
    elif (user == 3 and computer == 2):
        print("You win!")
    else:
        print("You loose(")
    run = False