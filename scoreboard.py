import pygame

class Scoreboard():

    def __init__(self, font: pygame.font.Font) -> None:
        self.font = font
        self.score = 0

    def scored(self) -> None:
        self.score += 1

    def show_score(self) -> pygame.Surface:
        return self.font.render(f"{self.score}", True, "white")
