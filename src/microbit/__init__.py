"""
Pins, images, sounds, temperature and volume
"""

from __future__ import annotations
from typing import Callable

from . import accelerometer, audio, compass, display, i2c, microphone, speaker, spi, uart


def run_every(callback: Callable = None, days: int = 0, h: int = 0, min: int = 0, s: int = 0, ms: int = 0) -> None:
    """
    Schedule to run a function at the interval specified by the time arguments V2 only.
    :param callback: Function to call at the provided interval. Omit when using as a decorator.
    :param days: Sets the day mark for the scheduling.
    :param h: Sets the hour mark for the scheduling.
    :param min: Sets the minute mark for the scheduling.
    :param s: Sets the second mark for the scheduling.
    :param ms: Sets the millisecond mark for the scheduling.
    """


def panic(n: int) -> None:
    """
    Enter a panic mode.
    :param n: An arbitrary integer <= 255 to indicate a status.
    """


def reset() -> None:
    """
    Restart the board.
    """


def scale(value: int | float, from_: tuple[int | float, int | float], to: tuple[int | float, int | float]) -> int | float:
    """
    Converts a value from a range to a floating point range.
    :param value: A number to convert.
    :param from_: A tuple to define the range to convert from.
    :param to: A tuple to define the range to convert to.
    :return: The value converted to the to range.
    """


def sleep(n: int) -> None:
    """
    Wait for n milliseconds.
    :param n: The number of milliseconds to wait
    """


def running_time() -> int:
    """
    Get the running time of the board.
    :return: The number of milliseconds since the board was switched on or restarted.
    """


def temperature() -> int:
    """
    Get the temperature of the micro:bit in degrees Celcius.
    :return: Return the temperature
    """


def set_volume(v: int) -> None:
    """
    Sets the volume.
    :param v: a value between 0 (low) and 255 (high).
    """


class Button:
    """
    The class for the buttons button_a and button_b.
    """

    def is_pressed(self) -> bool:
        """
        Check if the button is pressed.
        :return: True if the specified button **button** is pressed, and False otherwise.
        """

    def was_pressed(self) -> bool:
        """
        Check if the button was pressed since the device started or the last time this method was called.
        :return: True if the specified button **button** was pressed, and False otherwise
        """

    def get_presses(self) -> int:
        """
        Get the running total of button presses, and resets this total to zero before returning.
        :return: The number of presses since the device started or the last time this method was called
        """


button_a: Button
button_b: Button


class MicroBitDigitalPin:
    """
    A digital pin.
    """

    NO_PULL = 0
    PULL_UP = 1
    PULL_DOWN = 2

    def read_digital(self) -> int:
        """
        Get the digital value of the pin.
        :return: 1 if the pin is high, and 0 if it's low.
        """

    def write_digital(self, value: int) -> None:
        """
        Set the digital value of the pin.
        :param value: 1 to set the pin high or 0 to set the pin low
        """

    def set_pull(self, value: int) -> None:
        """
        Set the pull state to one of three possible values: PULL_UP, PULL_DOWN or NO_PULL.
        :param value: The pull state from the relevant pin
        """

    def get_pull(self) -> int:
        """
        Get the pull state on a pin.
        :return: NO_PULL, PULL_DOWN, or PULL_UP
        """

    def get_mode(self) -> str:
        """
        Returns the pin mode.
        :return: "unused", "analog", "read_digital", "write_digital", "display", "button", "music", "audio", "touch", "i2c", or "spi"
        """

    def write_analog(self, value: int | float) -> None:
        """
        Output a PWM signal on the pin, with the duty cycle proportional to value.
        :param value: An integer or a floating point number between 0 (0% duty cycle) and 1023 (100% duty).
        """

    def set_analog_period(self, period: int) -> None:
        """
        Set the period of the PWM signal being output to period in milliseconds.
        :param period: The period in milliseconds with a minimum valid value of 1ms.
        """

    def set_analog_period_microseconds(self, period: int) -> None:
        """
        Set the period of the PWM signal being output to period in microseconds.
        :param period: The period in microseconds with a minimum valid value of 256µs.
        """


class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """
    A pin with analog and digital features.
    """

    def read_analog(self) -> int:
        """
        Read the voltage applied to the pin.
        :return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V).
        """


class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """
    A pin with analog, digital and touch features.
    """

    CAPACITIVE = 0
    RESISTIVE = 1

    def is_touched(self) -> bool:
        """
        Check if the pin is being touched.
        :return: True if the pin is being touched with a finger, otherwise return False.
        """

    def set_touch_mode(self, value: int) -> None:
        """
        Set the touch mode for the pin.
        :param value: CAPACITIVE or RESISTIVE from the relevant pin.
        """


pin0: MicroBitTouchPin
pin1: MicroBitTouchPin
pin2: MicroBitTouchPin
pin3: MicroBitAnalogDigitalPin
pin4: MicroBitAnalogDigitalPin
pin5: MicroBitDigitalPin
pin6: MicroBitDigitalPin
pin7: MicroBitDigitalPin
pin8: MicroBitDigitalPin
pin9: MicroBitDigitalPin
pin10: MicroBitAnalogDigitalPin
pin11: MicroBitDigitalPin
pin12: MicroBitDigitalPin
pin13: MicroBitDigitalPin
pin14: MicroBitDigitalPin
pin15: MicroBitDigitalPin
pin16: MicroBitDigitalPin
pin17: MicroBitDigitalPin
pin18: MicroBitDigitalPin
pin19: MicroBitDigitalPin
pin20: MicroBitDigitalPin

pin_logo: MicroBitTouchPin
pin_speaker: MicroBitDigitalPin


class Image:
    """
    An image to show on the micro:bit LED display.
    """

    HEART: Image
    HEART_SMALL: Image
    HAPPY: Image
    SMILE: Image
    SAD: Image
    CONFUSED: Image
    ANGRY: Image
    ASLEEP: Image
    SURPRISED: Image
    SILLY: Image
    FABULOUS: Image
    MEH: Image
    YES: Image
    NO: Image
    CLOCK12: Image
    CLOCK11: Image
    CLOCK10: Image
    CLOCK9: Image
    CLOCK8: Image
    CLOCK7: Image
    CLOCK6: Image
    CLOCK5: Image
    CLOCK4: Image
    CLOCK3: Image
    CLOCK2: Image
    CLOCK1: Image
    ARROW_N: Image
    ARROW_NE: Image
    ARROW_E: Image
    ARROW_SE: Image
    ARROW_S: Image
    ARROW_SW: Image
    ARROW_W: Image
    ARROW_NW: Image
    TRIANGLE: Image
    TRIANGLE_LEFT: Image
    CHESSBOARD: Image
    DIAMOND: Image
    DIAMOND_SMALL: Image
    SQUARE: Image
    SQUARE_SMALL: Image
    RABBIT: Image
    COW: Image
    MUSIC_CROTCHET: Image
    MUSIC_QUAVER: Image
    MUSIC_QUAVERS: Image
    PITCHFORK: Image
    XMAS :Image
    PACMAN: Image
    TARGET: Image
    TSHIRT: Image
    ROLLERSKATE: Image
    DUCK: Image
    HOUSE: Image
    TORTOISE: Image
    BUTTERFLY: Image
    STICKFIGURE: Image
    GHOST: Image
    SWORD: Image
    GIRAFFE: Image
    SKULL: Image
    UMBRELLA: Image
    SNAKE: Image
    SCISSORS: Image
    ALL_CLOCKS: list[Image]
    ALL_ARROWS: list[Image]


    def __init__(self, string: str) -> None:
        """
        Create an image from a string describing which LEDs are lit.
        :param string: Consist of digits 0-9 arranged into lines, describing the image
        """

    def __int__(self, width: int = 5, height: int = 5, buffer: bytearray | None = None) -> None:
        """
        Create an empty image with width columns and height rows.
        :param width: Optional width of the image
        :param height: Optional height of the image
        :param buffer: Optional array or bytes of width×height integers in range 0-9 to initialize the image
        """

    def width(self) -> int:
        """
        Get the number of columns.
        :return: The number of columns in the image
        """

    def height(self) -> int:
        """
        Get the number of rows.
        :return: The number of rows in the image
        """

    def set_pixel(self, x: int, y: int, value: int):
        """
        Set the brightness of a pixel.
        :param x: The column number
        :param y: The row number
        :param value: The brightness as an integer between 0 (dark) and 9 (bright)
        """

    def get_pixel(self, x: int, y: int) -> int:
        """
        Get the brightness of a pixel.
        :param x: The column number
        :param y: The row number
        :return: The brightness as an integer between 0 and 9
        """

    def shift_left(self, n: int) -> 'Image':
        """
        Create a new image by shifting the picture left.
        :param n: The number of columns to shift by
        :return: The shifted image
        """

    def shift_right(self, n: int) -> 'Image':
        """
        Create a new image by shifting the picture right.
        :param n: The number of columns to shift by
        :return: The shifted image
        """

    def shift_up(self, n: int) -> 'Image':
        """
        Create a new image by shifting the picture up.
        :param n: The number of rows to shift by
        :return: The shifted image
        """

    def shift_down(self, n: int) -> 'Image':
        """
        Create a new image by shifting the picture down.
        :param n: The number of rows to shift by
        :return: The shifted image
        """

    def crop(self, x: int, y: int, w: int, h: int) -> 'Image':
        """
        Create a new image by cropping the picture.
        :param x: The crop offset column
        :param y: The crop offset row
        :param w: The crop width
        :param h: The crop height
        :return: The new image
        """

    def copy(self) -> 'Image':
        """
        Create an exact copy of the image.
        :return: The new image
        """

    def invert(self) -> 'Image':
        """
        Create a new image by inverting the brightness of the pixels in the source image.
        :return: The new image.
        """

    def fill(self, value) -> None:
        """
        Set the brightness of all the pixels in the image.
        :param value: The new brightness as a number between 0 (dark) and 9 (bright).
        """

    def blit(self, src: 'Image', x: int, y: int, w: int, h: int, xdest: int = 0, ydest: int = 0) -> None:
        """
        Copy an area from another image into this image.
        :param src: The source image
        :param x: The starting column offset in the source image
        :param y: The starting row offset in the source image
        :param w: The number of columns to copy
        :param h: The number of rows to copy
        :param xdest: The column offset to modify in this image
        :param ydest: The row offset to modify in this image
        """


class SoundEvent:
    LOUD: SoundEvent
    QUIET: SoundEvent


class Sound:
    """
    The built-in sounds
    """

    GIGGLE: Sound
    HAPPY: Sound
    HELLO: Sound
    MYSTERIOUS: Sound
    SAD: Sound
    SLIDE: Sound
    SOARING: Sound
    SPRING: Sound
    TWINKLE: Sound
    YAWN: Sound