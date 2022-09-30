import pygame
from Game import Game
from utils import initialize_screen


def main() -> None:
    """Main initialize function, only execute when `__main__`
    """
    # logger.debug("Python version: {}", str(sys.version))
    # logger.debug("Pygame version: {}", str(pygame.version.ver))
    # logger.debug("Current Process ID: {}", str(os.getpid()))
    # logger.debug("Current Parent Process ID: {}", str(os.getppid()))

    pygame.init()
    # logger.info("Pygame initialized")

    pygame.font.init()
    # logger.info("Pygame font module initialized")

    pygame.mixer.init()
    # logger.info("Pygame mixer module initialized")

    screen = initialize_screen(1280, 720)
    # logger.info("Initialized screen")

    pygame.display.set_caption("Swish and Frick")
    # logger.debug("Set window title to: {}", str(pygame.display.get_caption()[0]))

    try:
        game = Game(screen)
        game.run()
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()