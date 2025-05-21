import re

def escape_mentions(text: str) -> str:
    return re.sub(r"@(everyone|here|[!&]?[0-9]{17,20})", "@\u200b\\1", text)

def raw_mentions(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"<@!?([0-9]+)>", text)]

def raw_channel_mentions(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"<#([0-9]+)>", text)]

def raw_role_mentions(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"<@&([0-9]+)>", text)]
