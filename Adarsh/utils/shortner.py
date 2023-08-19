import re
import os
import asyncio
from info import LONG_DROPLINK_URL, SHORTENER_API
shortz = shortzy.Shortzy(SHORTENER_API, "dtglinks.in")
async def get_shortlink(link):
    if SHORTENER_API:
        if LONG_DROPLINK_URL == "True" or LONG_DROPLINK_URL is True:
            return await shortz.get_quick_link(link)
        else:
            return await shortz.convert(link, silently_fail=False)
    return link
