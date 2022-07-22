import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, pos: pygame.Vector2):
        super().__init__()
        self.img = image
        self.rect = image.get_rect(topleft = pos)