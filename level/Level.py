import pygame


class Level:
    _instances = set()

    def __init__(self, name):
        self.__class__._instances.add(self)

        self.name = name

        self.grid_width = 5
        self.grid_height = 5
        self.grid = []

        self.source = None

        self.sprite_group = pygame.sprite.Group()

    def update(self):
        # for y in range(self.grid_height):
        #     for x in range(self.grid_width-1):
        #         i = y * self.grid_width + x
        #         if self.grid[i]._filled:
        #             self.grid[i + 1]._filled = True
        self.sprite_group.update()

    def initialize_sprite_group(self):
        for cell in self.grid:
            self.sprite_group.add(cell)

    def draw(self, screen: pygame.Surface):
        self.sprite_group.draw(screen)

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for cell in self.grid:
                if cell.clicked(event.pos) and not cell.locked:
                    cell.rotate()

    def get_level_name(self):
        pass

    @classmethod
    def get_instances(cls):
        return cls._instances
