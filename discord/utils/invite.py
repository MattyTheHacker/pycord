import re

def resolve_invite(invite):
    """
    Resolves an invite from a :class:`~discord.Invite`, URL or code.
    """
    from ..invite import Invite  # circular import

    if isinstance(invite, Invite):
        return invite.code
    rx = r"(?:https?\:\/\/)?discord(?:\.gg|(?:app)?\.com\/invite)\/(.+)"
    m = re.match(rx, invite)
    if m:
        return m.group(1)
    return invite
