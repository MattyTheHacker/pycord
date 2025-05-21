from operator import attrgetter
from typing import Any, Callable, Iterable, TypeVar
T = TypeVar("T")

def find(predicate: Callable[[T], Any], seq: Iterable[T]) -> T | None:
    for element in seq:
        if predicate(element):
            return element
    return None

def get(iterable: Iterable[T], **attrs: Any) -> T | None:
    _all = all
    attrget = attrgetter
    if len(attrs) == 1:
        k, v = attrs.popitem()
        pred = attrget(k.replace("__", "."))
        for elem in iterable:
            if pred(elem) == v:
                return elem
        return None
    converted = [
        (attrget(attr.replace("__", ".")), value) for attr, value in attrs.items()
    ]
    for elem in iterable:
        if _all(pred(elem) == value for pred, value in converted):
            return elem
    return None
