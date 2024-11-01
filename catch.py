import pygame, simpleGE, random

class Turtle(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("turtle.jpg")
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("leaf.jpg")
        self.turtle = Turtle(self)
        
        self.sprite = [self.turtle]
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()