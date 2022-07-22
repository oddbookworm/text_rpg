from typing import Callable

from .gameobject import GameObject

class GameCharacter(GameObject):
    def __init__(self, image: pygame.Surface, pos: pygame.Vector2) -> None:
        super.__init__(self, image, pos)
        self._interaction = None
    
    def set_interaction(self, interaction: Callable[..., bool] -> None:
        self._interaction = interaction
        
    def interact(self, *args, **kwargs) -> bool:
        success = self._interaction(*args, **kwargs)