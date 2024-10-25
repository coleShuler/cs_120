import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Banana?")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("Yellow")

    banana = pygame.image.load("banana.png")
    banana = banana.convert_alpha()
    banana = pygame.transform.scale(banana, (100, 100))
    
    banana2 = pygame.image.load("banana.png")
    banana2 = banana.convert_alpha()
    banana2 = pygame.transform.scale(banana, (100, 100))
    
    banana3 = pygame.image.load("banana.png")
    banana3 = banana.convert_alpha()
    banana3 = pygame.transform.scale(banana, (100, 100))
    
    banana_x = 320
    banana_y = 50
    
    banana2_x = 220
    banana2_y = 200
    
    banana3_x = 220
    banana3_y = 200

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        banana_y += 1
        if banana_y > screen.get_height():
            banana_y = -1

        


        banana_y += 5
        if banana_y > screen.get_height():
            banana_y = 0
            
        banana2_x += 80
        if banana2_x > screen.get_height():
            banana2_x = 0
            
            
        banana3_y += 15
        if banana3_y > screen.get_height():
            banana3_y = 0

        banana3_x += 80
        if banana3_x > screen.get_height():
            banana3_x = 0


        screen.blit(background, (0, 0))
        screen.blit(banana, (banana_x, banana_y))
        screen.blit(banana2, (banana2_x, banana2_y))
        screen.blit(banana3, (banana3_x, banana3_y))
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()