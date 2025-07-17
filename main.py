import pygame
from constants import *
from player import Player

def main():
    # print("Starting Asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    black = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Allows user to exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill(black)

        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()

        # Set framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
