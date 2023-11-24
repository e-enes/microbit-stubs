"""
Measure the acceleration of the micro:bit and recognise gestures
"""


def get_x() -> int:
    """
    Get the acceleration measurement in the **x** axis in milli-g.
    :return: A positive or negative integer depending on direction in the range +/- 2000mg.
    """


def get_y() -> int:
    """
    Get the acceleration measurement in the **y** axis in milli-g.
    :return: A positive or negative integer depending on direction in the range +/- 2000mg.
    """


def get_z() -> int:
    """
    Get the acceleration measurement in the **z** axis in milli-g.
    :return: A positive or negative integer depending on direction in the range +/- 2000mg.
    """


def get_values() -> tuple[int, int, int]:
    """
    Get the acceleration measurements in all axes at once as a tuple.
    :return: A three-element tuple of integers ordered as **X**, **Y**, **Z**, each value a positive or negative integer depending on direction in the range +/- 2000mg
    """


def get_strength() -> int:
    """
    Get the acceleration measurement of all axes combined, as a positive integer. This is the Pythagorean sum of the **X**, **Y** and **Z** axes.
    :return: The combined acceleration strength of all the axes, in milli-g.
    """


def current_gesture() -> str:
    """
    Get the name of the current gesture.
    :return: The current gesture *("up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake")*.
    """


def is_gesture(name: str) -> bool:
    """
    Check if the named gesture is currently active.
    :param name: The gesture name *("up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake")*.
    :return: **True** if the gesture is active, **False** otherwise.
    """


def was_gesture(name: str) -> bool:
    """
    Check if the named gesture was active since the last call.
    :param name: The gesture name *("up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake")*.
    :return: **True** if the gesture was active since the last call, **False** otherwise.
    """


def get_gestures() -> tuple[str, ...]:
    """
    Return a tuple of the gesture history.
    :return: The history as a tuple, most recent last.
    """


def set_range(value: int) -> None:
    """
    Set the accelerometer sensitivity range, in g (standard gravity), to the closest values supported by the hardware, so it rounds to either **2**, **4**, or **8** g.
    :param value: New range for the accelerometer, an integer in **g**.
    """