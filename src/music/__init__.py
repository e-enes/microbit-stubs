"""
Create and play melodies
"""

from __future__ import annotations
from microbit import MicroBitDigitalPin, pin0

DADADADUM: tuple
ENTERTAINER: tuple
PRELUDE: tuple
ODE: tuple
NYAN: tuple
RINGTONE: tuple
FUNK: tuple
BLUES: tuple
BIRTHDAY: tuple
WEDDING: tuple
FUNERAL: tuple
PUNCHLINE: tuple
PYTHON: tuple
BADDY: tuple
CHASE: tuple
BA_DING: tuple
WAWAWAWAA: tuple
JUMP_UP: tuple
JUMP_DOWN: tuple
POWER_UP: tuple
POWER_DOWN: tuple


def set_tempo(ticks: int = 4, bpm: int = 120) -> None:
    """
    Sets the approximate tempo for playback.
    :param ticks: The number of ticks constituting a beat.
    :param bpm: An integer determining how many beats per minute.
    """


def get_tempo() -> tuple[int, int]:
    """
    Gets the current tempo as a tuple of integers: (ticks, bpm).
    :return: The temp as a tuple with two integer values, the ticks then the beats per minute.
    """


def play(music: tuple, pin: 'MicroBitDigitalPin' | None = pin0, wait: bool = True, loop: bool = False) -> None:
    """
    Plays music.
    :param music: Music specified in a special notation
    :param pin: The output pin for use with an external speaker (default pin0), None for no sound.
    :param wait: If wait is set to True, this function is blocking.
    :param loop: If loop is set to True, the tune repeats until stop is called or the blocking call is interrupted.
    """


def pitch(frequency: int, duration: int = -1, pin: 'MicroBitDigitalPin' = pin0, wait: bool = True) -> None:
    """
    Play a note.
    :param frequency: An integer frequency
    :param duration: A millisecond duration. If negative then sound is continuous until the next call or a call to stop.
    :param pin: Optional output pin (default pin0).
    :param wait: If wait is set to True, this function is blocking.
    """


def stop(pin: 'MicroBitDigitalPin' = pin0) -> None:
    """
    Stops all music playback on the built-in speaker and any pin outputting sound.
    :param pin: An optional argument can be provided to specify a pin
    """


def reset() -> None:
    """
    Resets ticks, bpm, duration and octave to their default values.
    """