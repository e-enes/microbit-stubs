"""
Communicate with devices using the serial peripheral interface (SPI) bus
"""

from . import MicroBitDigitalPin, pin13, pin14, pin15


def init(baudrate: int = 1000000, bits: int = 8, mode: int = 0, sclk: 'MicroBitDigitalPin' = pin13, mosi: 'MicroBitDigitalPin' = pin15, miso: 'MicroBitDigitalPin' = pin14) -> None:
    """
    Initialize SPI communication.
    :param baudrate: The speed of communication.
    :param bits: The width in bits of each transfer. Currently only **bits=8** is supported. However, this may change in the future.
    :param mode: Determines the combination of clock polarity and phase
    :param sclk: sclk pin (default 13)
    :param mosi: mosi pin (default 15)
    :param miso: miso pin (default 14)
    """


def read(nbytes: int) -> bytes:
    """
    Read bytes.
    :param nbytes: Maximum number of bytes to read.
    :return: The bytes read.
    """


def write(buffer: bytes) -> None:
    """
    Write bytes to the bus.
    :param buffer: A buffer to read data from.
    """


def write_readinto(out: bytes, in_: bytes) -> None:
    """
    Write the out buffer to the bus and read any response into the in_ buffer.
    :param out: The buffer to write any response to.
    :param in_: The buffer to read data from.
    """