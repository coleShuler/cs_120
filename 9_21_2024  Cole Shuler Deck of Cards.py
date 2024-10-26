import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)

def initCards():

    cardDB = []
    for i in range(NUMCARDS):
        cardDB.append(0)
    return cardDB

def showDB(cardDB):

    for cardNum, location in enumerate(cardDB):
        print(f"{cardNum:3}. {getCardName(cardNum):20} {HANDS[location]}")

def getCardName(cardNum):
    
    suit = cardNum // 13
    rank = cardNum % 13
    name = f"{RANKNAME[rank]} or {SUITNAME[suit]}"
    return name

def assignCard(cardDB, picked):
    
    cardNum = random.randrange(NUMCARDS)
    cardDB[cardNum] = picked
    
def showHand(cardDB, picked):
    print()
    print(f"cards in {HANDS[picked]}'s hand")
    for cardNum, location in enumerate(cardDB):
        if location == picked:
            print (f"  {getCardName(cardNum)}")

main()


