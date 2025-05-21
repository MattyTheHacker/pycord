"""
discord.utils




"""

from .invite import resolve_invite
from .template import resolve_template
from .markdown import remove_markdown, escape_markdown
from .mentions import escape_mentions, raw_mentions, raw_channel_mentions, raw_role_mentions
from .time import parse_time, sleep_until, utcnow, compute_timedelta
from .snowflake import snowflake_time, time_snowflake, generate_snowflake
from .chunking import as_chunks
from .search import find, get
from .deprecation import warn_deprecated, deprecated
from .oauth import oauth_url
from .formatting import format_dt
from .autocomplete import basic_autocomplete
from .params import filter_params
from .doc import copy_doc

__all__ = [
    "resolve_invite",
    "resolve_template",
    "remove_markdown",
    "escape_markdown",
    "escape_mentions",
    "raw_mentions",
    "raw_channel_mentions",
    "raw_role_mentions",
    "parse_time",
    "sleep_until",
    "utcnow",
    "compute_timedelta",
    "snowflake_time",
    "time_snowflake",
    "generate_snowflake",
    "as_chunks",
    "find",
    "get",
    "warn_deprecated",
    "deprecated",
    "oauth_url",
    "format_dt",
    "basic_autocomplete",
    "filter_params",
    "copy_doc",
]


