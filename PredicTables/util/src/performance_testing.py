import time
from typing import Callable, Any


def time_fn(fn: Callable[..., Any], *args: tuple, **kwargs: dict) -> float:
    """
    Times the execution of a function. Returns the time in seconds.

    Parameters
    ----------
    fn : Callable[..., Any]
        The function to time. Can be any function, including a lambda function.
    args : tuple
        The arguments to pass to the function. Should be in the form of a tuple.
    kwargs : dict
        The keyword arguments to pass to the function. Should be in the form of a dictionary.
    """
    start = time.time()  # start timer
    fn(*args, **kwargs)  # run function
    end = time.time()  # end timer
    return end - start  # return time elapsed
