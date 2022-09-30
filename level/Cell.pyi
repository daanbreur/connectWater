from typing import List

import pygame.surface

class Cell:
    def __init__(self, x: int, y: int, sprite: str, filled_sprite: str, connections: List[bool], locked: bool, source: bool, finish: bool):
        self.x: int
        self.y: int

        self.connections: List[bool]
        self.locked: bool
        self.source: bool
        self.finish: bool

        self._normal_sprite: str
        self._filled_sprite: str

        self.image: pygame.Surface
        self.rect: pygame.Rect

    def update_coords(self, x: int, y: int) -> None: ...
    def clicked(self, mouse_pos: tuple[int, int]) -> bool: ...
    def rotate(self) -> None: ...