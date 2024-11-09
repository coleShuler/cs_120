import pygame, random, simpleGE

class Leaf(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("leaf.jpg")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Turtle(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("turtle.png")
        self.setSize(65, 30)
        self.position = (320, 400)
        self.moveSpeed = 3
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed     
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("BG.jpg")
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 25
        self.score = 0
        
        self.sndLeaf = simpleGE.Sound("crunch.wav")
        
        self.turtle = Turtle(self)
        self.leafs = []
        for i in range(10):
            self.leafs.append(Leaf(self))
            
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        self.sprites = [self.turtle,
                        self.leafs,
                        self.lblScore, 
                        self.lblTime]
        
    def process(self):
        for leaf in self.leafs:
            if self.turtle.collidesWith(leaf):
                self.sndLeaf.play()
                leaf.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()

class Title(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("BG.jpg")
        
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
                
        if title.response == "Play":    
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
            
            
if __name__ == "__main__":
    main()