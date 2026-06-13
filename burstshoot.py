from weapon import Weapon
from shot import Shot
import pygame

class BurstShoot(Weapon):
    def __init__(self, owner, cooldown, bullet_speed, bullet_radius, burst_cooldown, burst_length):
        super().__init__(owner, cooldown, bullet_speed, bullet_radius)
        self.burst_cooldown = burst_cooldown
        self.burst_timer = 0.0
        self.burst_length = burst_length
        self.burst_counter = 0
        self.timer = 0.0
        self.in_burst = False

    def update(self, dt):
        if self.timer > 0.0:
            self.timer -= dt

        if self.in_burst:
            self.burst_timer -= dt

            if self.burst_timer <= 0 and self.burst_counter < self.burst_length:
                self.fire_bullet()
                self.burst_timer = self.burst_cooldown
                self.burst_counter += 1

            if self.burst_counter == self.burst_length:
                self.in_burst = False
                self.burst_counter = 0
                self.timer = self.cooldown


    def shoot(self):
        if self.timer <= 0.0 and not self.in_burst:
            self.in_burst = True
                


                  

    