import re

def resolve_template(code):
    """
    Resolves a template code from a :class:`~discord.Template`, URL or code.
    """
    from ..template import Template  # circular import

    if isinstance(code, Template):
        return code.code
    rx = r"(?:https?\:\/\/)?discord(?:\.new|(?:app)?\.com\/template)\/(.+)"
    m = re.match(rx, code)
    if m:
        return m.group(1)
    return code
