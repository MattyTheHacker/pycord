from typing import Callable, TypeVar
from inspect import signature as _signature
T = TypeVar("T")
def copy_doc(original: Callable) -> Callable[[T], T]:
    def decorator(overridden: T) -> T:
        overridden.__doc__ = original.__doc__
        overridden.__signature__ = _signature(original)  # type: ignore
        return overridden
    return decorator
