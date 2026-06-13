from circleshape import *
import pygame

class Shot(CircleShape):

    def __init__(self, x, y, shot_radius):
        super().__init__(x, y, shot_radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt