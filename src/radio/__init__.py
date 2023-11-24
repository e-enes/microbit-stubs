"""
Communicate between micro:bits with the built-in radio
"""

from __future__ import annotations


RATE_1MBIT = 0
RATE_2MBIT = 1


def on() -> None:
    """
    Turns the radio on.
    """


def off() -> None:
    """
    Turns off the radio, saving power and memory.
    """


def config(length: int = 32, queue: int = 3, channel: int = 7, power: int = 6, address: int = 0x75626974, group: int = 0, data_rate: int = RATE_1MBIT) -> None:
    """
    Configures the radio.
    :param length: (default=32) defines the maximum length, in bytes, of a message sent via the radio. It can be up to 251 bytes long (254 - 3 bytes for S0, LENGTH and S1 preamble).
    :param queue: (default=3) specifies the number of messages that can be stored on the incoming message queue. If there are no spaces left on the queue for incoming messages, then the incoming message is dropped.
    :param channel: (default=7) an integer value from 0 to 83 (inclusive) that defines an arbitrary "channel" to which the radio is tuned. Messages will be sent via this channel and only messages received via this channel will be put onto the incoming message queue. Each step is 1MHz wide, based at 2400MHz.
    :param power: (default=6) is an integer value from 0 to 7 (inclusive) to indicate the strength of signal used when broadcasting a message. The higher the value the stronger the signal, but the more power is consumed by the device. The numbering translates to positions in the following list of dBm (decibel milliwatt) values: -30, -20, -16, -12, -8, -4, 0, 4.
    :param address: (default=0x75626974) an arbitrary name, expressed as a 32-bit address, that's used to filter incoming packets at the hardware level, keeping only those that match the address you set.
    :param group: (default=0) an 8-bit value (0-255) used with the address when filtering messages. Conceptually, "address" is like a house/office address and "group" is like the person at that address to which you want to send your message.
    :param data_rate: (default=radio.RATE_1MBIT) indicates the speed at which data throughput takes place.
    """


def reset() -> None:
    """
    Reset the settings to their default values.
    """


def send_bytes(message: bytes) -> None:
    """
    Sends a message containing bytes.
    :param message: The bytes to send.
    """


def receive_bytes() -> bytes | None:
    """
    Receive the next incoming message on the message queue.
    :return: The message bytes if any, otherwise None.
    """


def receive_bytes_into(buffer: bytearray) -> int | None:
    """
    Copy the next incoming message on the message queue into a buffer.
    :param buffer: The target buffer. The message is truncated if larger than the buffer.
    :return: None if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer).
    """


def send(message: str) -> None:
    """
    Sends a message string.
    :param message: The string to send.
    """


def receive() -> str | None:
    """
    Returns whatever was sent.
    :return: The message with the prepended bytes stripped and converted to a string.
    :raise ValueError: if conversion to string fails.
    """


def receive_full() -> tuple | None:
    """
    Returns a tuple containing three values representing the next incoming message on the message queue.
    :return: None if there is no message, otherwise a tuple of length three with the bytes, strength and timestamp values.
    """