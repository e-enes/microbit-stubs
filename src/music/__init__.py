"""
Create and play melodies
"""

import typing
import microbit

DADADADUM: typing.Tuple = tuple()
ENTERTAINER: typing.Tuple = tuple()
PRELUDE: typing.Tuple = tuple()
ODE: typing.Tuple = tuple()
NYAN: typing.Tuple = tuple()
RINGTONE: typing.Tuple = tuple()
FUNK: typing.Tuple = tuple()
BLUES: typing.Tuple = tuple()
BIRTHDAY: typing.Tuple = tuple()
WEDDING: typing.Tuple = tuple()
FUNERAL: typing.Tuple = tuple()
PUNCHLINE: typing.Tuple = tuple()
PYTHON: typing.Tuple = tuple()
BADDY: typing.Tuple = tuple()
CHASE: typing.Tuple = tuple()
BA_DING: typing.Tuple = tuple()
WAWAWAWAA: typing.Tuple = tuple()
JUMP_UP: typing.Tuple = tuple()
JUMP_DOWN: typing.Tuple = tuple()
POWER_UP: typing.Tuple = tuple()
POWER_DOWN: typing.Tuple = tuple()


def set_tempo(ticks: int = 4, bpm: int = 120) -> None:
    """
    Sets the approximate tempo for playback.
    :param ticks: The number of ticks constituting a beat.
    :param bpm: An integer determining how many beats per minute.
    """


def get_tempo() -> typing.Tuple[int, int]:
    """
    Gets the current tempo as a tuple of integers: (ticks, bpm).
    :return: The temp as a tuple with two integer values, the ticks then the beats per minute.
    """


def play(music: tuple, pin: typing.Union['microbit.MicroBitDigitalPin', None] = 'pin0', wait: bool = True, loop: bool = False) -> None:
    """
    Plays music.
    :param music: Music specified in a special notation
    :param pin: The output pin for use with an external speaker (default pin0), None for no sound.
    :param wait: If wait is set to True, this function is blocking.
    :param loop: If loop is set to True, the tune repeats until stop is called or the blocking call is interrupted.
    """


def pitch(frequency: int, duration: int = -1, pin: 'microbit.MicroBitDigitalPin' = 'pin0', wait: bool = True) -> None:
    """
    Play a note.
    :param frequency: An integer frequency
    :param duration: A millisecond duration. If negative then sound is continuous until the next call or a call to stop.
    :param pin: Optional output pin (default pin0).
    :param wait: If wait is set to True, this function is blocking.
    """


def stop(pin: 'microbit.MicroBitDigitalPin' = 'pin0') -> None:
    """
    Stops all music playback on the built-in speaker and any pin outputting sound.
    :param pin: An optional argument can be provided to specify a pin
    """


def reset() -> None:
    """
    Resets ticks, bpm, duration and octave to their default values.
    """