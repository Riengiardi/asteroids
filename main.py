import pygame, sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
from logger import log_state, log_event

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    gameover = False
    gameover_font = pygame.font.Font("font.ttf", 64)

    drawable, updatable, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    a_field = AsteroidField()

    while True:
        # logger function from boot.dev
        log_state()

        for event in pygame.event.get():
            # check for quiting by X
            if event.type == pygame.QUIT:
                return

        if not gameover:
            screen.fill("black")
            
            for d in drawable:
                d.draw(screen)
            
            dt = clock.tick(60) / 1000
            updatable.update(dt)

            for a in asteroids:
                if p1.collides_with(a):
                    log_event("player_hit")
                    gameover = True
                    
                for s in shots:
                    if s.collides_with(a):
                        log_event("asteroid_shot")
                        a.split()
                        s.kill()

            pygame.display.flip()
        else:
            screen.fill("black")
            gameover_text = gameover_font.render("Game over!", True, "white")
            screen.blit(gameover_text, gameover_text.get_rect(center=SCREEN_CENTER))
            pygame.display.flip()



if __name__ == "__main__":
    main()
