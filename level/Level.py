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
        self.finish = None

        self.sprite_group = pygame.sprite.Group()

    def get_neighbors(self, cell):
        neighbors = {"up": None, "right": None, "down": None, "left": None}
        i = self.grid_width*cell.y+cell.x

        if i >= self.grid_width:
            neighbors["up"] = self.grid[i-self.grid_width]

        if i % self.grid_width != 0:
            neighbors["left"] = self.grid[i-1]

        if (i+1) % self.grid_width != 0:
            neighbors["right"] = self.grid[i+1]

        if i + self.grid_width < (self.grid_width*self.grid_height):
            neighbors["down"] = self.grid[i+self.grid_width]

        return neighbors

    def flow_water(self, cell):
        if cell._filled: return
        cell._filled = True

        neighbors = self.get_neighbors(cell)
        print(cell.__dict__, neighbors)
        if neighbors["up"] != None:
            if neighbors["up"].connections[2] and cell.connections[0]:
                self.flow_water(neighbors["up"])
        if neighbors["right"] != None:
            if neighbors["right"].connections[3] and cell.connections[1]:
                self.flow_water(neighbors["right"])
        if neighbors["down"] != None:
            if neighbors["down"].connections[1] and cell.connections[2]:
                self.flow_water(neighbors["down"])
        if neighbors["left"] != None:
            if neighbors["left"].connections[1] and cell.connections[3]:
                self.flow_water(neighbors["left"])

    def update(self):
        for cell in self.grid:
            cell._filled = False
        self.flow_water(self.source)

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
        return self.name

    @classmethod
    def get_instances(cls):
        return cls._instances
