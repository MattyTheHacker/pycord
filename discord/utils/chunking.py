from typing import Iterator, AsyncIterator, TypeVar, overload, Union
T = TypeVar("T")
_Iter = Union[Iterator[T], AsyncIterator[T]]

@overload
def as_chunks(iterator: Iterator[T], max_size: int) -> Iterator[list[T]]: ...
@overload
def as_chunks(iterator: AsyncIterator[T], max_size: int) -> AsyncIterator[list[T]]: ...

def _chunk(iterator: Iterator[T], max_size: int) -> Iterator[list[T]]:
    ret = []
    n = 0
    for item in iterator:
        ret.append(item)
        n += 1
        if n == max_size:
            yield ret
            ret = []
            n = 0
    if ret:
        yield ret

async def _achunk(iterator: AsyncIterator[T], max_size: int) -> AsyncIterator[list[T]]:
    ret = []
    n = 0
    async for item in iterator:
        ret.append(item)
        n += 1
        if n == max_size:
            yield ret
            ret = []
            n = 0
    if ret:
        yield ret

def as_chunks(iterator: _Iter[T], max_size: int) -> _Iter[list[T]]:
    if max_size <= 0:
        raise ValueError("Chunk sizes must be greater than 0.")
    from collections.abc import AsyncIterator as AI
    if isinstance(iterator, AI):
        return _achunk(iterator, max_size)
    return _chunk(iterator, max_size)
