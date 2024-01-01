import re
import os
import asyncio
import shortzy
from ..vars import Var
from pyshorteners import Shortener
shortz = shortzy.Shortzy(Var.SHORTENER_API, "dtglinks.in")
async def get_shortlink(online_link):
    if Var.SHORTENER_API:
        if Var.LONG_DROPLINK_URL == "True" or Var.LONG_DROPLINK_URL is True:
            link= await shortz.get_quick_link(online_link)
        else:
            link= await shortz.convert(online_link, silently_fail=False)
    return link
