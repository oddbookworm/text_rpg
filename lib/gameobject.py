import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, pos: pygame.Vector2) -> None:
        super().__init__()
        self.img = image
        self.rect = image.get_rect(topleft = pos)
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.img, self.rect)
        
    def update(self, offset: pygame.Vector2) -> None:
        self.rect.move(offset)