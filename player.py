import circleshape
import pygame
from constants import *
from logger import log_event
from weapon import Weapon
from singleshoot import *
from burstshoot import *

class Player(circleshape.CircleShape):

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0
        self.speed: float = 0.0
        self.weapons: list[Weapon] = [
            BurstShoot(self, 0.2, 500, 4, 0.035, 3), 
            SingleShoot(self, 0.3, 400, 6)
        ]
        self.current_weapon = self.weapons[0]


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # rotation accounting for fps
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * self.speed * dt
        self.position += rotated_with_speed_vector

    def update(self, dt: float) -> None:

        super().update(dt)
        self.move(dt)
        self.current_weapon.update(dt)

        keys = pygame.key.get_pressed()

        # rotation controls
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # accelerated movement controls including decceleration logic when left untouched
        if keys[pygame.K_w]:
            if self.speed < PLAYER_SPEED: self.speed += 120 * dt
        elif keys[pygame.K_s]:
            if self.speed > -PLAYER_SPEED: self.speed -= 120 * dt
        else:
            if self.speed > 0: 
                self.speed -= 120 * dt
            if self.speed < 0:
                self.speed += 120 * dt
            
        # weapon controls
        if keys[pygame.K_SPACE]:
            self.current_weapon.shoot()
        if keys[pygame.K_1]:
            self.current_weapon = self.weapons[0]
        if keys[pygame.K_2]:
            self.current_weapon = self.weapons[1]

        