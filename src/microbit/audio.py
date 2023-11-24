"""
Play sounds using the micro:bit
"""

from __future__ import annotations
from . import Sound, MicroBitTouchPin, pin0


def play(source: 'Sound' | 'SoundEffect' | 'AudioFrame', wait: bool = True, pin: 'MicroBitTouchPin' = pin0, return_pin: 'MicroBitTouchPin' | None = None) -> None:
    """
    Play a built-in sound, sound effect or custom audio frames.
    :param source: A built-in **Sound** such as **Sound.GIGGLE**, a **SoundEffect** or sample data as an iterable of **AudioFrame** objects.
    :param wait: If **wait** is **True**, this function will block until the sound is complete.
    :param pin: An optional argument to specify the output pin can be used to override the default of **pin0**. If we do not want any sound to play we can use **pin=None**.
    :param return_pin: Specifies a differential edge connector pin to connect to an external speaker instead of ground. This is ignored for the V2 revision.
    """


def is_playing() -> bool:
    """
    Check whether a sound is playing.
    :return: **True** if audio is playing, otherwise **False**.
    """


def stop() -> None:
    """
    Stop all audio playback.
    """


class SoundEffect:
    """
    A sound effect, composed by a set of parameters configured via the constructor or attributes.
    """

    WAVEFORM_SINE = 0
    WAVEFORM_SAWTOOTH = 1
    WAVEFORM_TRIANGLE = 2
    WAVEFORM_SQUARE = 3
    WAVEFORM_NOISE = 4

    FX_TREMOLO = 0
    FX_VIBRATO = 1
    FX_WARBLE = 2
    FX_NONE = 3

    SHAPE_LINEAR = 0
    SHAPE_CURVE = 1
    SHAPE_LOG = 2

    def __init__(self, freq_start: int = 500, freq_end: int = 2500, duration: int = 500, vol_start: int = 255, vol_end: int = 0, waveform: int = WAVEFORM_SQUARE, fx: int = FX_NONE, shape: int = SHAPE_LOG):
        """
        :param freq_start: Start frequency in Hertz (Hz), a number between **0** and **9999**.
        :param freq_end: End frequency in Hertz (Hz), a number between **0** and **9999**.
        :param duration: Duration of the sound in milliseconds, a number between **0** and **9999**.
        :param vol_start: Start volume value, a number between **0** and **255**.
        :param vol_end: End volume value, a number between **0** and **255**.
        :param waveform: Type of waveform shape, one of the waveform constants.
        :param fx: Effect to add on the sound, one of the FX constants.
        :param shape: The type of the interpolation curve, one of the shape constants.
        """

    def copy(self) -> 'SoundEffect':
        """
        Create a copy of this **SoundEffect**.
        :return: A copy of the SoundEffect.
        """


class AudioFrame:
    """
    An **AudioFrame** object is a list of 32 samples each of which is a unsigned byte (whole number between 0 and 255).
    """

    def copyfrom(self, other: 'AudioFrame') -> None:
        """
        Overwrite the data in this **AudioFrame** with the data from another **AudioFrame** instance.
        :param other: **AudioFrame** instance from which to copy the data.
        """