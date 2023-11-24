"""
Make the micro:bit talk, sing and make other speech like sounds
"""

from __future__ import annotations
from microbit import MicroBitDigitalPin, pin0


def translate(words: str) -> str:
    """
    Translate English words to phonemes.
    :param words: A string of English words.
    :return: A string containing a best guess at the appropriate phonemes to pronounce.
    """


def pronounce(phonemes: str, pitch: int = 64, speed: int = 72, mouth: int = 128, throat: int = 128, pin: 'MicroBitDigitalPin' | None = pin0) -> None:
    """
    Pronounce phonemes.
    :param phonemes: The string of phonemes to pronounce
    :param pitch: A number representing the pitch of the voice
    :param speed: A number representing the speed of the voice
    :param mouth: A number representing the mouth of the voice
    :param throat: A number representing the throat of the voice
    :param pin: Optional argument to specify the output pin can be used to override the default of pin0.
    """


def say(words: str, pitch: int = 64, speed: int = 72, mouth: int = 128, throat: int = 128, pin: 'MicroBitDigitalPin' | None = pin0) -> None:
    """
    Say English words.
    :param words: The string of words to say
    :param pitch: A number representing the pitch of the voice
    :param speed: A number representing the speed of the voice
    :param mouth: A number representing the mouth of the voice
    :param throat: A number representing the throat of the voice
    :param pin: Optional argument to specify the output pin can be used to override the default of pin0.
    """


def sing(phonemes, pitch: int = 64, speed: int = 72, mouth: int = 128, throat: int = 128, pin: 'MicroBitDigitalPin' | None = pin0) -> None:
    """
    Sing phonemes.
    :param phonemes: The string of words to sing
    :param pitch: A number representing the pitch of the voice
    :param speed: A number representing the speed of the voice
    :param mouth: A number representing the mouth of the voice
    :param throat: A number representing the throat of the voice
    :param pin: Optional argument to specify the output pin can be used to override the default of pin0.
    """