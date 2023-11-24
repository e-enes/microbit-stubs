"""
Use the built-in compass
"""


def calibrate() -> None:
    """
    Starts the calibration process.
    """


def is_calibrated() -> bool:
    """
    Check is the compass is calibrated.
    :return: **True** if the compass has been successfully calibrated, **False** otherwise.
    """


def clear_calibration() -> None:
    """
    Undoes the calibration, making the compass uncalibrated again.
    """


def get_x() -> int:
    """
    Get the magnetic field strength on the **x** axis.
    :return: A positive or negative integer in nano tesla representing the magnitude and direction of the field.
    """


def get_y() -> int:
    """
    Get the magnetic field strength on the **y** axis.
    :return: A positive or negative integer in nano tesla representing the magnitude and direction of the field.
    """


def get_z() -> int:
    """
    Get the magnetic field strength on the **z** axis.
    :return: A positive or negative integer in nano tesla representing the magnitude and direction of the field.
    """


def heading() -> int:
    """
    Get the compass heading.
    :return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0.
    """


def get_field_strength() -> int:
    """
    Get the magnitude of the magnetic field around the device.
    :return: An integer indication of the magnitude of the magnetic field in nano tesla.
    """