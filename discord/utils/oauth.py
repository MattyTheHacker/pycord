from typing import Any, Iterable

def oauth_url(
    client_id: int | str,
    *,
    permissions: Any = None,
    guild: Any = None,
    redirect_uri: str = None,
    scopes: Iterable[str] = None,
    disable_guild_select: bool = False,
) -> str:
    url = f"https://discord.com/oauth2/authorize?client_id={client_id}"
    url += f"&scope={'+'.join(scopes or ('bot',))}"
    if permissions is not None:
        url += f"&permissions={permissions.value}"
    if guild is not None:
        url += f"&guild_id={guild.id}"
    if redirect_uri is not None:
        from urllib.parse import urlencode
        url += f"&response_type=code&{urlencode({'redirect_uri': redirect_uri})}"
    if disable_guild_select:
        url += "&disable_guild_select=true"
    return url
