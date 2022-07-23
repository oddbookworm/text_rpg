from typing import Callable

import pygame

from .gameobject import GameObject


class GameCharacter(GameObject):
    def __init__(self, image: pygame.Surface, pos: pygame.Vector2) -> None:
        super().__init__(image, pos)
        self._interaction = None

    def set_interaction(self, interaction: Callable[..., bool]) -> None:
        self._interaction = interaction

    def interact(self, *args, **kwargs) -> bool:
        if self._interaction is None:
            return False

        success = self._interaction(*args, **kwargs)
        return success
