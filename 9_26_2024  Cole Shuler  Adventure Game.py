def main():
    game = gameState()
    keepGoing = True
    nextState = "water"
    while keepGoing:
        nextState = playGame(game, nextState)
        if nextState == "quit":
            keepGoing = False

def gameState():
    game = {
    "water": ["You're in a desert and you think you see water, what do you do", "Go to the water", "marriage", "Take a nap", "marriage"], 
    "marriage": ["The water was just a marriage, oh no!", "Quit", "quit", "Restart", "water"], 
    "stay": ["You stay put for a while and fall asleep when you wake up you're in a jail cell, what's the play...", "Ask for help", "help", "Go back to bed", "bed"], 
    "help": ["You ask for help and they decide to kill you right there and then...", "Quit", "quit", "Restart", "water"], 
    "bed": ["After your nice rest, the guards decide to give you one of two things, what would you like?", "Pillow", "pillow", "Blanket", "blanket"], 
    "pillow": ["They realize they can't let you get any more rest and don't give it to you, that was a waste.", "Quit", "quit", "Restart", "water"], 
    "blanket": ["They give you the blanket and you found a way to escape with the blanket! What do you do?", "Escape", "escape", "More sleep!", "sleep"], 
    "sleep": ["Why on earth would you want to take another nap?", "Quit", "quit", "Restart", "restart"], 
    "escape": ["You use the blanket to do a magic trick and disappear, the guards slip the door open. What do you do!", "Tackle the guard", "tackle", "Go through the door", "door"], 
    "tackle": ["You tackle the guard and the door closes right after. Now you're locked in with him...", "Quit", "quit", "Restart", "water"], 
    "door": ["You exit through the door and lock the guard in. what direction do you go?", "Right", "right", "Left", "left"], 
    "left": ["We all know right is right...", "Quit", "quit", "Restart", "water"], 
    "right": ["Thats the Exit! Quickly!", "Go through the door", "exit", "The pillow...", "end"], 
    "exit": ["You exit the building and realize you forgot the pillow. That sucks...", "Quit", "quit", "Restart", "water"], 
    "end": ["You Finally got your pillow, now you can get some more sleep...", "Quit", "quit", "restart", "water"],
    }
    return game

def playGame(game, currentState):
    (description, option1, o1, option2, o2) = game[currentState]
    
    print(f"""
    {description}
    1: {option1}
    2: {option2}
    """)
    
    Choice = input("select 1 or 2: ")

    if Choice == "1":
        nextState = o1
    elif Choice == "2":
        nextState = o2
    else:
        print ("Not a valid input. Please enter '1' or '2.'")
        nextState = currentState

    return nextState
main()