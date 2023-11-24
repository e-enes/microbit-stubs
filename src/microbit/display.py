"""
Show text, images and animations on the 5×5 LED display
"""

from __future__ import annotations
from . import Image


def get_pixel(x: int, y: int) -> int:
    """
    Get the brightness of the LED at column x and row y.
    :param x: The display column (0..4)
    :param y: The display row (0..4)
    :return: A number between 0 (off) and 9 (bright)
    """


def set_pixel(x: int, y: int, value: int) -> None:
    """
    Set the brightness of the LED at column **x** and row **y**.
    :param x: The display column (0..4)
    :param y: The display row (0..4)
    :param value: The brightness between 0 (off) and 9 (bright)
    """


def clear() -> None:
    """
    Set the brightness of all LEDs to 0 (off).
    """


def show(image: str | int | 'Image' | list['Image'], delay: int = 400, wait: bool = True, loop: bool = False, clear: bool = False) -> None:
    """
    Shows images, letters or digits on the LED display.
    :param image: A string, number, Image or list of Images to show.
    :param delay: Each letter, digit or image is shown with **delay** milliseconds between them.
    :param wait: If **wait** is **True**, this function will block until the animation is finished, otherwise the animation will happen in the background.
    :param loop: If **loop** is **True**, the animation will repeat forever.
    :param clear: If **clear** is **True**, the display will be cleared after the sequence has finished.
    """


def scroll(text: str, delay: int = 150, wait: bool = True, loop: bool = False, monospace: bool = False) -> None:
    """
    Scrolls a number or text on the LED display.
    :param text: The string to scroll.
    :param delay: The **delay** parameter controls how fast the text is scrolling.
    :param wait: If **wait** is **True**, this function will block until the animation is finished, otherwise the animation will happen in the background.
    :param loop: If **loop** is **True**, the animation will repeat forever.
    :param monospace: If **monospace** is **True**, the characters will all take up 5 pixel-columns in width, otherwise there will be exactly 1 blank pixel-column between each character as they scroll.
    """


def on() -> None:
    """
    Turn on the LED display.
    """


def off() -> None:
    """
    Turn off the LED display.
    """


def is_on() -> bool:
    """
    Check whether the LED display is enabled.
    :return: **True** if the display is on, otherwise returns **False**.
    """


def read_light_level() -> int:
    """
    Read the light level.
    :return: An integer between 0 and 255 representing the light level, with larger meaning more light.
    """