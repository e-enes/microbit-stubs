"""
Communicate with a device using a serial interface
"""

from __future__ import annotations

EVEN = 0
ODD = 1


def init(baudrate: int = 9600, bits: int = 8, parity: int | None = None, stop: int = 1, tx: 'MicroBitTouchPin' | None = None, rx: 'MicroBitTouchPin' | None = None) -> None:
    """
    Initialize serial communication.
    :param baudrate: The speed of communication.
    :param bits: The size of bytes being transmitted. micro:bit only supports 8.
    :param parity: How parity is checked, None, uart.ODD or uart.EVEN.
    :param stop: The number of stop bits, has to be 1 for micro:bit.
    :param tx: Transmitting pin.
    :param rx: Receiving pin.
    """


def any() -> bool:
    """
    Check if any data is waiting.
    :return: **True** if any data is waiting, else *$False**.
    """


def read(nbytes: int | None = None) -> bytearray | None:
    """
    Read bytes.
    :param nbytes: If nbytes is specified then read at most that many bytes, otherwise read as many bytes as possible
    :return: A bytes object or None on timeout
    """


def readinto(buf: bytearray, nbytes: int | None = None) -> int | None:
    """
    Read bytes into the **buf**.
    :param buf: The buffer to write to.
    :param nbytes: If nbytes is specified then read at most that many bytes, otherwise read len(buf) bytes.
    :return: Number of bytes read and stored into buf or None on timeout.
    """


def readline() -> str:
    """
    Read a line, ending in a newline character.
    :return: The line read or None on timeout. The newline character is included in the returned bytes.
    """


def write(buf: bytearray) -> int | None:
    """
    Write a buffer to the bus.
    :param buf: A bytes object or a string.
    :return: The number of bytes written, or None on timeout.
    """