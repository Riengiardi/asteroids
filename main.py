import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version {pygame.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        # logger function from boot.dev
        log_state()

        for event in pygame.event.get():
            # check for quiting by X
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        # makes sure that the time between frames is limited to .0166666 (60fps)
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
