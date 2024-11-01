import pygame
from constants import *


def main():
    pygame.init()
    TICK = 60
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0, 0, 0))
        pygame.display.flip()
        clock.tick(TICK)
        dt = clock.tick(TICK) / 1000
          
if __name__ == "__main__":
    main()