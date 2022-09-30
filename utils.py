"""Utilities for handling inventory, layers, screen, pyinstaller and more"""
from __future__ import annotations
from typing import TYPE_CHECKING, Union

import os
import sys
import logging
import pygame

from constants import RESOURCES_DIR

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


def resource_path(relative_path: Union[Path, str]) -> str:
    """Get absolute path to resource, for dev and for PyInstaller

    Args:
        relative_path (Union[Path, str]): relative path to resource

    Returns:
        str: full path to resource
    """
    try:
        base_path = sys._MEIPASS  # pylint: disable=W0212 disable=E1101
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def initialize_screen(width: int, height: int) -> pygame.Surface:
    """Initialize new screen with given width and height

    Args:
        width (int): width of screen
        height (int): height of screen

    Returns:
        pygame.Surface: new screen instance
    """
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    logger.info("Initialized screen with size {}", screen.get_size())
    return screen


def load_image(filename: str) -> pygame.Surface:
    """Load image from file

    Args:
        filename (str): relative path to image file

    Returns:
        pygame.Surface: image surface loaded from file
    """
    return pygame.image.load(resource_path(RESOURCES_DIR / filename))


def get_font_at_size(font_name="Level Up Level Up.otf", font_size=16) -> pygame.font.Font:
    """Get font at given size

    Args:
        font_name (str, optional): filename for the font. Defaults to "Level Up Level Up.otf".
        font_size (int, optional): fontsize for the font. Defaults to 16.

    Returns:
        pygame.font.Font: font instance at given size and font
    """
    return pygame.font.Font(resource_path(RESOURCES_DIR / "fonts" / font_name), font_size)