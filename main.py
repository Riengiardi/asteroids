import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version {pygame.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    drawable, updatable, asteroids = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    a_field = AsteroidField()

    while True:
        # logger function from boot.dev
        log_state()

        for event in pygame.event.get():
            # check for quiting by X
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
        
        updatable.update(dt)

        pygame.display.flip()

        # makes sure that the time between frames is limited to .0166666 (60fps)
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
