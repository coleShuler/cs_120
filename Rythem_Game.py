import pygame, random, simpleGE


class Title(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        
        self.response = "Play"
        
        self.title = simpleGE.MultiLabel()
        self.title.textLines = [
        "You are a Turtle!",
        "Move with the arrow keys",
        "Catch as many Leaf's as you can!",
        "This game is timed, so be aware",
        "Have Fun :D"]
        
        self.title.center = (320, 170)
        self.title.size = (500, 250)
        
        self.prevScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 350)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (up)"
        self.btnPlay.center = (200, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (down)"
        self.btnQuit.center = (450, 400)
        
        self.sprites = [self.title,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
        
    def process(self):
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()

        if self.isKeyPressed(pygame.K_UP):
            self.response = "Play"
            self.stop()
        if self.isKeyPressed(pygame.K_DOWN):
            self.response = "Quit"
            self.stop()



def main():
    keepGoing = True
    score = 0
    while keepGoing:
        
        title = Title(score)
        title.start()
        
        title = Title(score)
        title.start()
                
        if title.response == "Play":    
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
        
if __name__ == "__main__":
    main()