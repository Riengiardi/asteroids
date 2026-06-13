from shot import Shot
import pygame

class Weapon():

    def __init__(self, owner, cooldown: float, bullet_speed: int, bullet_radius: int) -> None:
        self.owner = owner
        self.cooldown = cooldown
        self.bullet_speed = bullet_speed
        self.bullet_radius = bullet_radius

    def fire_bullet(self) -> None:
        bullet = Shot(self.owner.position.x, self.owner.position.y, self.bullet_radius)
        bullet.velocity = pygame.Vector2(0, 1)
        bullet.velocity = bullet.velocity.rotate(self.owner.rotation)
        bullet.velocity *= self.bullet_speed

    def update(self, dt: float) -> None:
        pass #override

    def shoot(self) -> None:
        pass #override   