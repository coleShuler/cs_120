import random

print("Welcome to my guessing game!")

chances = 7
number = random.randint(1,100)
keepGoing = True

while keepGoing == True:
    if chances == 0:
        keepGoing = False
        print(f"You lost! My number was {number}")
    if keepGoing == True:
        choice = input("Pick a number between 1 - 100.")
    if choice != number:
        chances -= 1
    if int(choice) > number:
        print(f"That is to high! You have {chances} tries left!")
    if int(choice) < number:
        print(f"That is to low! You have {chances} tries left!")
    if int(choice) == number:
        keepGoing = False
        print("You Win!")
    