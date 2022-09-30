import os

from SingletonType import SingletonType
from constants import RESOURCES_DIR
from level.Cell import Cell
from level.Level import Level
from utils import resource_path
import yaml

class LevelManager(metaclass=SingletonType):
    def __init__(self):
        self.levels = []
        self.current_level = None
        self.load_level_files(resource_path(RESOURCES_DIR / "levels"))

    def add_level(self, level):
        self.levels.append(level)

    def get_current_level(self):
        return self.current_level

    def get_current_level_name(self):
        return self.current_level.name

    def set_current_level(self, index):
        self.current_level = self.levels[index]

    def load_level_files(self, folder):
        for file in os.listdir(folder):
            with open(resource_path(RESOURCES_DIR / "levels" / file), 'r') as f:
                data = yaml.safe_load(f)

                level = Level(data['level-properties']['name'])
                level.grid_width = data['map-properties']['width']
                level.grid_height = data['map-properties']['height']
                level.grid = [None]*(level.grid_width*level.grid_height)

                for cellData in data['map']:
                    is_source = cellData["source"]
                    is_finish = cellData["finish"]

                    x = cellData["x"]
                    y = cellData["y"]

                    cell = Cell(x, y, cellData["empty_sprite"], cellData["filled_sprite"], cellData["connections"], cellData["locked"], is_source, is_finish)
                    if is_source:
                        level.source = cell
                    if is_finish:
                        level.finish = cell

                    level.grid[level.grid_width*y+x] = cell

                level.initialize_sprite_group()
                self.add_level(level)
