"""
Manage the power modes of the micro:bit (V2 only)
"""

from __future__ import annotations


def off() -> None:
    """
    Power down the board to the lowest possible power mode.
    """


def deep_sleep(ms: int | None = None, wake_on=None, run_every: bool = True) -> None:
    """
    Set the micro:bit into a low power mode where it can wake up and continue operation.
    :param ms: A time in milliseconds to wait before it wakes up.
    :param wake_on: A single instance or a tuple of pins and/or buttons to wake up the board, e.g. deep_sleep(wake_on=button_a) or deep_sleep(wake_on=(pin0, pin2, button_b)).
    :param run_every: A boolean to configure if the functions scheduled with microbit.run_every will continue to run while it sleeps.
    """