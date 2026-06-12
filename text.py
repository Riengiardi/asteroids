import pygame
from collections.abc import Callable

class Text():

    def __init__(self, font_path : str, font_size: int, content_provider: Callable[[], str], x_pos: int, y_pos: int) -> None:
        self.font: pygame.font.Font = pygame.font.Font(font_path, font_size)
        self.content_provider = content_provider
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self, screen: pygame.Surface) -> None:
        text = self.content_provider()
        rendered = self.font.render(text, True, 'white')
        center = rendered.get_rect(center=(self.x_pos, self.y_pos))
        screen.blit(rendered, center)
