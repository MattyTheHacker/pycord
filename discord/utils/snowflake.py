import datetime
from typing import Any

DISCORD_EPOCH = 1420070400000

def snowflake_time(id: int) -> datetime.datetime:
    timestamp = ((id >> 22) + DISCORD_EPOCH) / 1000
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)

def time_snowflake(dt: datetime.datetime, high: bool = False) -> int:
    discord_millis = int(dt.timestamp() * 1000 - DISCORD_EPOCH)
    return (discord_millis << 22) + (2**22 - 1 if high else 0)

def generate_snowflake(dt: datetime.datetime | None = None) -> int:
    dt = dt or datetime.datetime.now(datetime.timezone.utc)
    return int(dt.timestamp() * 1000 - DISCORD_EPOCH) << 22 | 0x3FFFFF
