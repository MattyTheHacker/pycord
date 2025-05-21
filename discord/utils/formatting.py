import datetime
from typing import Literal

TimestampStyle = Literal["f", "F", "d", "D", "t", "T", "R"]

def format_dt(
    dt: datetime.datetime | datetime.time, /, style: TimestampStyle | None = None
) -> str:
    if isinstance(dt, datetime.time):
        dt = datetime.datetime.combine(datetime.datetime.now(), dt)
    if style is None:
        return f"<t:{int(dt.timestamp())}>"
    return f"<t:{int(dt.timestamp())}:{style}>"
