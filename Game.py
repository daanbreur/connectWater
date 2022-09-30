import pygame

from SingletonType import SingletonType
from level.Cell import Cell
from level.Level import Level
from level.LevelManager import LevelManager
from utils import initialize_screen


class Game(metaclass=SingletonType):
    """Contains whole game
    """

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.running = False
        # self.game_state = GameState.MAIN_MENU

        # self.toast_manager: ToastManager = ToastManager(self.screen)
        self.level_manager = LevelManager()
        self.level_manager.set_current_level(0)

        # self.menus = {
        #     "mainmenu": MainMenu(self),
        #     "ingame": Ingame(self),
        #     "settings": SettingsMenu(self),
        #     "pausemenu": PausedMenu(self),
        # }

    def draw(self) -> None:
        """Draws current active menu
        """

        self.level_manager.get_current_level().draw(self.screen)

        # if self.game_state == GameState.MAIN_MENU:
        #     self.menus["mainmenu"].draw(self.screen)
        # if self.game_state == GameState.SETTINGS:
        #     self.menus["settings"].draw(self.screen)
        # if self.game_state == GameState.PAUSE_MENU:
        #     self.menus["pausemenu"].draw(self.screen)
        # if self.game_state == GameState.IN_GAME:
        #     self.menus["ingame"].draw(self.screen)
        #     for puzzle in self.puzzles.values():
        #         if puzzle.active:
        #             puzzle.draw(self.screen)
        #     self.toast_manager.draw(self.screen)

    def handle_input(self) -> None:
        """Handle input for everything game related
        - Movement
        - Buttons
        - Resizes
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

            elif event.type == pygame.VIDEORESIZE:
                # logger.info("Resizing screen to {}x{}", event.w, event.h)
                self.screen = initialize_screen(event.w, event.h)

            self.level_manager.get_current_level().handle_input(event)

    def update(self, dt_: float) -> None:
        """Handle update cycle for everything game

        Args:
            dt_ (float): frame timedelta
        """
        self.level_manager.get_current_level().update()
        # self.menus["ingame"].update(dt_)

    def run(self) -> None:
        """Run 👏 The 👏 Game 👏 Loop 👏"""
        clock = pygame.time.Clock()
        self.running = True

        try:
            while self.running:
                dt_ = clock.tick() / 1000.0
                self.handle_input()
                self.update(dt_)
                self.draw()
                pygame.display.flip()
        except KeyboardInterrupt:
            self.running = False
