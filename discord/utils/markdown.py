import re

_MARKDOWN_ESCAPE_SUBREGEX = "|".join(
    r"\\{0}(?=([\s\S]*((?<!\\{0})\\{0})))".format(c) for c in ("*", "`", "_", "~", "|")
)
_MARKDOWN_ESCAPE_LINKS = r"""
\[  # matches link text
    [^\[\]]* # link text can contain anything but brackets
\]
\(  # matches link destination
    [^\(\)]+ # link destination cannot contain parentheses
\)"""
_MARKDOWN_ESCAPE_COMMON = rf"^>(?:>>)?\s|{{_MARKDOWN_ESCAPE_LINKS}}"
_MARKDOWN_ESCAPE_REGEX = re.compile(
    rf"(?P<markdown>{{_MARKDOWN_ESCAPE_SUBREGEX}}|{{_MARKDOWN_ESCAPE_COMMON}})",
    re.MULTILINE | re.X,
)
_URL_REGEX = r"(?P<url><[^: >]+:\/[^ >]+>|(?:https?|steam):\/\/[^\s<]+[^<.,:;\"'\]\s])"
_MARKDOWN_STOCK_REGEX = rf"(?P<markdown>[_\\~|\*`]|{{_MARKDOWN_ESCAPE_COMMON}})"

def remove_markdown(text: str, *, ignore_links: bool = True) -> str:
    def replacement(match):
        groupdict = match.groupdict()
        return groupdict.get("url", "")

    regex = _MARKDOWN_STOCK_REGEX
    if ignore_links:
        regex = f"(?:{_URL_REGEX}|{regex})"
    return re.sub(regex, replacement, text, 0, re.MULTILINE)

def escape_markdown(
    text: str, *, as_needed: bool = False, ignore_links: bool = True
) -> str:
    if not as_needed:
        def replacement(match):
            groupdict = match.groupdict()
            is_url = groupdict.get("url")
            if is_url:
                return is_url
            return f"\\{groupdict['markdown']}"

        regex = _MARKDOWN_STOCK_REGEX
        if ignore_links:
            regex = f"(?:{_URL_REGEX}|{regex})"
        return re.sub(regex, replacement, text, 0, re.MULTILINE | re.X)
    else:
        text = re.sub(r"\\", r"\\\\", text)
        return _MARKDOWN_ESCAPE_REGEX.sub(r"\\\1", text)
