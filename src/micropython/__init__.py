"""
MicroPython internals
"""


def const(expr):
    """
    Used to declare that the expression is a constant so that the compiler can optimise it.
    :param expr: A constant expression.
    """


def opt_level() -> int:
    """
    Get the current optimisation level for the compilation of scripts.
    :return: An integer representing the current level.
    """


def opt_level(level: int) -> None:
    """
    Sets the optimisation level for subsequent compilation of scripts.
    :param level: An integer optimisation level.
    """


def mem_info(verbose=None) -> None:
    """
    Print information about currently used memory.
    :param verbose: If the verbose argument is given then extra information is printed.
    """


def qstr_info(verbose=None) -> None:
    """
    Print information about currently interned strings.
    :param verbose: If the verbose argument is given then extra information is printed.
    """


def stack_use() -> int:
    """
    Return an integer representing the current amount of stack that is being used.
    :return: An integer representing current stack use.
    """


def heap_lock() -> None:
    """
    Lock the heap.
    """


def heap_unlock() -> None:
    """
    Unlock the heap.
    """


def kbd_intr(chr: int) -> None:
    """
    Set the character that will raise a KeyboardInterrupt exception.
    :param chr: Character code to raise the interrupt or -1 to disable capture of Ctrl-C.
    """