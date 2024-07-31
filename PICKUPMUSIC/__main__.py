import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from PICKUPMUSIC import LOGGER, app, userbot
from PICKUPMUSIC.core.call import Line
from PICKUPMUSIC.misc import sudo
from PICKUPMUSIC.plugins import ALL_MODULES
from PICKUPMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PICKUPMUSIC.plugins" + all_module)
    LOGGER("PICKUPMUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Line.start()
    try:
        await Line.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("PICKUPMUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Line.decorators()
    LOGGER("PICKUPMUSIC").info(
        "Line Music Bot Started Successfully"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("PICKUPMUSIC").info("Stopping Line Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
