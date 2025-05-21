import asyncio, itertools
from typing import Any, Awaitable, Callable, Iterable, Union

async def basic_autocomplete(
    values: Union[Iterable[Any], Callable], *, filter: Callable = None
):
    async def autocomplete_callback(ctx):
        _values = values
        if callable(_values):
            _values = _values(ctx)
        if asyncio.iscoroutine(_values):
            _values = await _values
        if filter is None:
            def _filter(ctx, item):
                item = getattr(item, "name", item)
                return str(item).lower().startswith(str(ctx.value or "").lower())
            gen = (val for val in _values if _filter(ctx, val))
        elif asyncio.iscoroutinefunction(filter):
            gen = (val for val in _values if await filter(ctx, val))
        elif callable(filter):
            gen = (val for val in _values if filter(ctx, val))
        else:
            raise TypeError("``filter`` must be callable.")
        return iter(itertools.islice(gen, 25))
    return autocomplete_callback
