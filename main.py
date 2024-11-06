import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *


def main():
    pygame.init()
    TICK = 60
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    dt = 0
    
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