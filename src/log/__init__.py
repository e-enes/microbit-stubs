"""
Log data to your micro:bit V2
"""

from __future__ import annotations

MILLISECONDS = 1
SECONDS = 2
MINUTES = 3
HOURS = 4
DAYS = 5


def set_labels(*labels: str, timestamp: int | None = SECONDS) -> None:
    """
    Set up the log file header.
    :param labels: Any number of positional arguments, each corresponding to an entry in the log header.
    :param timestamp: Select the timestamp unit that will be automatically added as the first column in every row. Timestamp values can be one of log.MILLISECONDS, log.SECONDS, log.MINUTES, log.HOURS, log.DAYS or None to disable the timestamp. The default value is log.SECONDS.
    """


def add(data_dictionary: dict) -> None:
    """
    Add a data row to the log by passing a dictionary of headers and values.
    :param data_dictionary: The data to log as a dictionary with a key for each header.
    """


def add(**kwargs) -> None:
    """
    Add a data row to the log using keyword arguments.
    """


def delete(full: bool = False) -> None:
    """
    Deletes the contents of the log, including headers.
    :param full: True selects a “full” erase and False selects the “fast” erase method.
    """


def set_mirroring(serial: bool) -> None:
    """
    Configure mirroring of the data logging activity to the serial output.
    :param serial: True enables mirroring data to the serial output.
    """