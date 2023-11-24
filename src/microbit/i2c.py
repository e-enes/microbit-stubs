"""
Communicate with devices using the I²C bus protocol
"""

from __future__ import annotations
from . import MicroBitDigitalPin, pin20, pin19


def init(freq: int = 100000, sda: 'MicroBitDigitalPin' = pin20, scl: 'MicroBitDigitalPin' = pin19) -> None:
    """
    Re-initialize a peripheral.
    :param freq: Clock frequency
    :param sda: sda pin (default 20)
    :param scl: scl pin (default 19)
    """


def scan() -> list[int]:
    """
    Scan the bus for devices.
    :return: A list of 7-bit addresses corresponding to those devices that responded to the scan.
    """


def read(addr: int, n: int) -> bytes:
    """
    Read bytes from a device.
    :param addr: The 7-bit address of the device
    :param n: The number of bytes to read
    :return: The bytes read
    """


def write(addr: int, buf: bytes | bytearray, repeat: bool = False) -> None:
    """
    Write bytes to a device.
    :param addr: The 7-bit address of the device
    :param buf: A buffer containing the bytes to write
    :param repeat: If **True**, no stop bit will be sent
    :return:
    """