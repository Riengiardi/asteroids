import pygame, sys
from particle import Particle
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
from text import *
from logger import log_state, log_event

def main():

    # base for running the window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # state for losing condition
    is_gameover = False
    lives = 3

    # text variables for content providers
    score = 0

    # text objects
    gameover_text = Text(GAME_FONT, 64, lambda: "Game Over!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    scoreboard = Text(GAME_FONT, 24, lambda: f"Score: {score}", SCREEN_WIDTH/2, 16)
    life_count = Text(GAME_FONT, 24, lambda: f"Lives: {lives}", SCREEN_WIDTH/2, SCREEN_HEIGHT - 16)

    # containers for different sprite types
    drawable, updatable, asteroids, shots = (pygame.sprite.Group(), 
                                             pygame.sprite.Group(), 
                                             pygame.sprite.Group(), 
                                             pygame.sprite.Group())
    
    # assigning sprites to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Particle.containers = (updatable, drawable)

    # helper function to clear and repopulate screen on death
    def start_new_game() -> tuple[Player, AsteroidField]:
        drawable.empty()
        updatable.empty()
        asteroids.empty()
        shots.empty()
        return Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), AsteroidField()


    # drawing player at the middle
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # asteroid field for generating asteroid
    a_field = AsteroidField()

    while True:
        # logger function from boot.dev
        log_state()

        for event in pygame.event.get():
            # check for quiting by X
            if event.type == pygame.QUIT:
                return

        if not is_gameover:
            screen.fill("black")

            scoreboard.draw(screen)
            life_count.draw(screen)
            
            for d in drawable:
                d.draw(screen)
            
            dt = clock.tick(60) / 1000
            updatable.update(dt)

            for a in asteroids:
                if p1.collides_with(a):
                    log_event("player_hit")
                    p1, a_field = start_new_game()
                    lives -= 1
                    if lives < 0:
                        is_gameover = True
                    
                    
                for s in shots:
                    if s.collides_with(a):
                        log_event("asteroid_shot")
                        score += 1
                        a.split()
                        s.kill()

            pygame.display.flip()
        else:
            screen.fill("black")
            gameover_text.draw(screen)
            pygame.display.flip()



if __name__ == "__main__":
    main()
