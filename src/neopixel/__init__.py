"""
Individually addressable RGB and RGBW LED strips
"""

from __future__ import annotations
from microbit import MicroBitDigitalPin


class NeoPixel:
    def __init__(self, pin: 'MicroBitDigitalPin', n: int, bpp: int = 3):
        """
        Initialise a new strip of neopixel LEDs controlled via a pin.
        :param pin: The pin controlling the neopixel strip.
        :param n: The number of neopixels in the strip.
        :param bpp: Bytes per pixel. For RGBW neopixel support, pass 4 rather than the default of 3 for RGB and GRB.
        """

    def clear(self) -> None:
        """
        Clear all the pixels.
        """

    def show(self) -> None:
        """
        Show the pixels.
        """

    def write(self) -> None:
        """
        Show the pixels (micro:bit V2 only).
        """

    def fill(self, colour: tuple) -> None:
        """
        Colour all pixels a given RGB/RGBW value.
        :param colour: A tuple of the same length as the number of bytes per pixel (bpp).
        """