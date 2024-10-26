import random

fortune = ["Never", "Maybe Not", "Most likely", "Maybe", "Yes", "No", "You betcha", "Abssolutely"]

print("1. Show fortunes")
print("2. Pick a fortune")
print("3. Get your fortune!")
choice = input("Select an option 1, 2, or 3: ")

if choice == "1":
    for i, value in enumerate(fortune):
        print(f"{i}: {value}")

if choice == "2":
    choice = input("Pick a number between 0 - 7: ")
    if choice == ("0"):
        print("Never")
    if choice == ("1"):
        print("Maybe not")
    if choice == ("2"):
        print("Most likely")
    if choice == ("3"):
        print("Maybe")
    if choice == ("4"):
        print("Yes")
    if choice == ("5"):
        print("No")
    if choice == ("6"):
        print("You betcha")
    if choice == ("7"):
        print("Abssolutely")
        
elif choice == "3":
    choice = input("What is your fortune: ")
    random.shuffle (fortune)
    eightBall = random.choice(fortune)
    print ("Your fortune is:", eightBall)