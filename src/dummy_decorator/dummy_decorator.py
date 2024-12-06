"""
Empty decorator.
"""

from functools import update_wrapper
from typing import Callable, TypeVar, Any

F = TypeVar('F', bound=Callable[..., Any])


def dummy_decorator(func: F) -> F:
    return update_wrapper(lambda *args, **kwargs: func(*args, **kwargs), func)
