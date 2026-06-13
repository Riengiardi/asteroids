from circleshape import CircleShape
from constants import *
import pygame, random, math
from logger import log_event
from particle import Particle

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        
        super().__init__(x, y, radius)

        self.shape: list[pygame.Vector2] = []

        for i in range(32):
            angle = (2 * math.pi * i) / 32
            r = radius + random.uniform(-radius * 0.05, radius * 0.05)
            
            self.shape.append(
                pygame.Vector2(
                    math.cos(angle) * r,
                    math.sin(angle) * r,
                )
            )

    def draw(self, screen):
        points: list[pygame.Vector2] = [self.position + p for p in self.shape]
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def explode(self):
        for i in range(0, 6):
            angle = random.uniform(0, 360)
            v_mul = random.uniform(1.6, 2.4)
            v_part = self.velocity.rotate(angle)
            particle = Particle(self.position.x, self.position.y, 2)
            particle.velocity = v_part * v_mul

    def split(self) -> None:

        self.kill()
        self.explode()

        if self.radius == ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1 * 1.2
        a2.velocity = vel2 * 1.2

