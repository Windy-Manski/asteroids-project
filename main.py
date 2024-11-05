import pygame
from constants import *
from circleshape import *
from player import *


def main():
    pygame.init()
    TICK = 60
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    
    while True:
        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)
        
        pygame.Surface.fill(screen, color=(0, 0, 0))
        
        for item in drawable:
            item.draw(screen) 
        

        pygame.display.flip()
        
        dt = clock.tick(TICK) / 1000 # FPS control
        


          
if __name__ == "__main__":
    main()