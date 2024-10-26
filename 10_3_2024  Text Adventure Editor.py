def main():
    game = gameState()
    nextState = "start"
    getMenuChoice()



def getMenuChoice():
    keepGoing = True
    print(""""
0: Play the current game
1: Load default game
2: Load a game file
3: Save the current game
4: Edit or add a node 
5: Exit
""")
    while keepGoing:
        menu = input("select from these options: ")
        if menu == "0":
            print("This will play the current game")
        if menu == "1":
            nextState = playGame(game, nextState)
            if nextState == "quit":
                keepGoing = False
        if menu == "2":
            print("This will load default game")
        if menu == "3":
            print("This will save the current game")
        if menu == "4":
            textFile()
        if menu == "5":
            keepGoing = False

def textFile():
    inFile = open("textAdventure.json", "r")
    textAdventure = json.load(inFile)
    adventureFile = input

    inFile.close()

main()



def gameState():
    game = {
    "start": ["Discription of your game","menuA", "nodeA", "menuB", "nodeB"] 
    }



def playGame(game, currentState):
    (description, menuA, nodeA, menuB, nodeB) = game[currentState]
    
    print(f"""
    {description}
    1: {option1}
    2: {option2}
    """)
    
    Choice = input("select 1 or 2: ")

    if Choice == "1":
        nextState = nodeA
    elif Choice == "2":
        nextState = nodeB
    else:
        print ("Not a valid input. Please enter '1' or '2.'")
        nextState = currentState

    return nextState



main()