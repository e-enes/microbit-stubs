"""
Respond to sound using the built-in microphone (V2 only).
"""

from __future__ import annotations
from . import SoundEvent


def current_event() -> 'SoundEvent':
    """
    Get the last recorded sound event.
    :return: The event, **SoundEvent('loud')** or **SoundEvent('quiet')**.
    """


def was_event(event: 'SoundEvent') -> bool:
    """
    Check if a sound was heard at least once since the last call.
    :param event: The event to check for, such as **SoundEvent.LOUD** or **SoundEvent.QUIET**
    :return: **True** if sound was heard at least once since the last call, otherwise **False**.
    """


def is_event(event: 'SoundEvent') -> bool:
    """
    Check the most recent sound event detected.
    :param event: The event to check for, such as **SoundEvent.LOUD** or **SoundEvent.QUIET**
    :return: **True** if sound was the most recent heard, **False** otherwise.
    """


def get_events() -> tuple['SoundEvent']:
    """
    Get the sound event history as a tuple.
    :return: A tuple of the event history with the most recent event last.
    """


def set_threshold(event: 'SoundEvent', value: int) -> None:
    """
    Set the threshold for a sound event.
    :param event: The event to check for, such as **SoundEvent.LOUD** or **SoundEvent.QUIET**
    :param value: The threshold level in the range 0-255.
    """


def sound_level() -> int:
    """
    Get the sound pressure level.
    :return: A representation of the sound pressure level in the range 0 to 255.
    """