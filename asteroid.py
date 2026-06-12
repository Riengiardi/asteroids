from circleshape import CircleShape
from constants import *
import pygame, random
from logger import log_event
from particle import Particle

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def explode(self):
        for i in range(0, 6):
            angle = random.uniform(0, 360)
            v_mul = random.uniform(1.6, 2.0)
            particle = Particle(self.position.x, self.position.y, 2)
            vel_p = self.velocity.rotate(angle)
            particle.velocity = vel_p * v_mul

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

