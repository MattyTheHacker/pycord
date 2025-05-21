import datetime, asyncio
from typing import Any, TypeVar

def parse_time(timestamp: str | None) -> datetime.datetime | None:
    if timestamp:
        return datetime.datetime.fromisoformat(timestamp)
    return None

def sleep_until(when: datetime.datetime, result: Any = None):
    delta = compute_timedelta(when)
    return asyncio.sleep(delta, result)

def utcnow() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)

def compute_timedelta(dt: datetime.datetime):
    if dt.tzinfo is None:
        dt = dt.astimezone()
    now = datetime.datetime.now(datetime.timezone.utc)
    return max((dt - now).total_seconds(), 0)
