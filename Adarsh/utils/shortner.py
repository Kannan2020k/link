import re
import os
import asyncio
from ..vars import Var
shortz = shortzy.Shortzy(SHORTENER_API, "dtglinks.in")
async def get_shortlink(link):
    if SHORTENER_API:
        if Var.LONG_DROPLINK_URL == "True" or Var.LONG_DROPLINK_URL is True:
            return await shortz.get_quick_link(link)
        else:
            return await shortz.convert(link, silently_fail=False)
    return link
