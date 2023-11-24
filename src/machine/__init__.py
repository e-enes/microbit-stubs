"""
Low-level utilities
"""

from microbit import MicroBitDigitalPin


def unique_id() -> bytes:
    """
    Get a byte string with a unique identifier of a board.
    :return: An identifier that varies from one board instance to another.
    """


def reset() -> None:
    """
    Reset the device in a manner similar to pushing the external RESET button.
    """


def freq() -> int:
    """
    Get the CPU frequency in hertz.
    :return: The CPU frequency.
    """


def disable_irq() -> int:
    """
    Disable interrupt requests.
    :return: The previous IRQ state which should be considered an opaque value
    """


def enable_irq(state: int) -> None:
    """
    Re-enable interrupt requests.
    :param state: The value that was returned from the most recent call to the disable_irq function.
    """


def time_pulse(pin: 'MicroBitDigitalPin', pulse_level: int, timeout_us: int = 1000000) -> int:
    """
    Time a pulse on a pin.
    :param pin: The pin to use
    :param pulse_level: 0 to time a low pulse or 1 to time a high pulse
    :param timeout_us: A microsecond timeout
    :return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match pulse_level, or -2 on timeout waiting for the pulse to end
    """