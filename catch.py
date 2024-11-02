import pygame, simpleGE, random

class Turtle(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("turtle.png")
        self.setSize(100, 50)
        self.position = (320, 400)
        self.moveSpeed = 3
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("leaf.jpg")
        self.turtle = Turtle(self)
        
        self.sprites  = [self.turtle]
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()