"""
Control the garbage collector
"""


def enable() -> None:
    """
    Enable automatic garbage collection.
    """


def disable() -> None:
    """
    Disable automatic garbage collection.
    """


def collect() -> None:
    """
    Run a garbage collection.
    """


def mem_alloc() -> int:
    """
    Get the number of bytes of heap RAM that are allocated.
    :return: The number of bytes allocated.
    """


def mem_free() -> int:
    """
    Get the number of bytes of available heap RAM, or -1 if this amount is not known.
    :return: The number of bytes free.
    """


def threshold() -> int:
    """
    Query the additional GC allocation threshold.
    :return:
    """


def threshold(amount: int) -> None:
    """
    Set the additional GC allocation threshold.
    :param amount: The number of bytes after which a garbage collection should be triggered.
    """