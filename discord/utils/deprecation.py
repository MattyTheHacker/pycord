import warnings, functools
from typing import Callable, Any

def warn_deprecated(
    name: str,
    instead: str | None = None,
    since: str | None = None,
    removed: str | None = None,
    reference: str | None = None,
    stacklevel: int = 3,
) -> None:
    warnings.simplefilter("always", DeprecationWarning)
    message = f"{name} is deprecated"
    if since:
        message += f" since version {since}"
    if removed:
        message += f" and will be removed in version {removed}"
    if instead:
        message += f", consider using {instead} instead"
    message += "."
    if reference:
        message += f" See {reference} for more information."
    warnings.warn(message, stacklevel=stacklevel, category=DeprecationWarning)
    warnings.simplefilter("default", DeprecationWarning)

def deprecated(
    instead: str | None = None,
    since: str | None = None,
    removed: str | None = None,
    reference: str | None = None,
    stacklevel: int = 3,
    *,
    use_qualname: bool = True,
) -> Callable:
    def actual_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            warn_deprecated(
                name=func.__qualname__ if use_qualname else func.__name__,
                instead=instead,
                since=since,
                removed=removed,
                reference=reference,
                stacklevel=stacklevel,
            )
            return func(*args, **kwargs)
        return decorated
    return actual_decorator
