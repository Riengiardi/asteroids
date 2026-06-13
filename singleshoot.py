from weapon import Weapon
import pygame

class SingleShoot(Weapon):

    def __init__(self, owner, cooldown, bullet_speed, bullet_radius):
        super().__init__(owner, cooldown, bullet_speed, bullet_radius)
        self.timer: float = 0.0

    def update(self, dt):
        if self.timer >= 0.0:
            self.timer -= dt

    def shoot(self):
        if self.timer <= 0.0:
            self.fire_bullet()
            self.timer = self.cooldown