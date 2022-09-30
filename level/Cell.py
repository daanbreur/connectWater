import pygame
from utils import load_image


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite, filled_sprite, connections, locked=False, source=False, finish=False):
        super().__init__()

        self.x = x
        self.y = y

        self.connections = connections
        self.locked = locked
        self.source = source
        self.finish = finish

        self._normal_sprite = sprite
        self._filled_sprite = filled_sprite
        self._filled = False
        self._rotation = 0

        self.image = load_image("./sprites/" + self._normal_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 2), int(self.image.get_height() * 2)))
        self.rect = self.image.get_rect()

    def update(self):
        if self._filled or self.source:
            self.image = load_image("./sprites/" + self._filled_sprite).convert_alpha()
            self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * 2), int(self.image.get_height() * 2)))
            self.image = pygame.transform.rotate(self.image, self._rotation)
            self.rect = self.image.get_rect()
        else:
            self.image = load_image("./sprites/" + self._normal_sprite).convert_alpha()
            self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * 2), int(self.image.get_height() * 2)))
            self.image = pygame.transform.rotate(self.image, self._rotation)
            self.rect = self.image.get_rect()

        self.rect.topleft = (480 + self.x * 64, 200 + self.y * 64)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def rotate(self):
        self._rotation = (self._rotation+90)%360
        self.image = pygame.transform.rotate(self.image, self._rotation)
        self.connections = self.connections[1:] + [self.connections[0]]