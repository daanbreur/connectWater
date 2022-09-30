from __future__ import annotations
from typing import TYPE_CHECKING, List

import pygame

from Cell import Cell

class Level:
    _instances: set

    def __init__(self, name: str):
        self.name: str
        self.grid_width: int
        self.grid_height: int
        self.grid: List[Cell]
        self.sprite_group: pygame.sprite.Group

    def update(self) -> None: ...
    def update_sprite_group(self) -> None: ...
    def draw(self, screen: pygame.Surface) -> None: ...
    def handle_input(self, event: pygame.event.Event) -> None: ...
    def get_level_name(self) -> str: ...

    @classmethod
    def get_instances(cls) -> set[Level]: ...
