import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import LOGGER, app, userbot
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    # Check if assistant client variables are defined
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()  # Perform sudo initialization

    try:
        # Fetch global banned users and add to BANNED_USERS set
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        # Fetch banned users and add to BANNED_USERS set
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()  # Start the main bot client

    # Import all modules
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("AnonXMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()  # Start the userbot client
    await Anony.start()  # Start the Anony client

    try:
        # Attempt to stream a video call
        await Anony.stream_call("https://telegra.ph/file/cba632240b79207bf8a9c.mp4")
    except NoActiveGroupCall:
        # Log error if no active group call and exit
        LOGGER("AnonXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await Anony.decorators()  # Setup decorators

    # Log a message indicating bot is running
    LOGGER("AnonXMusic").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝐂𝐡𝐢𝐧𝐧𝐚 ♨️\n╚═════ஜ۩۞۩ஜ════╝")
        
    await idle()  # Keep the bot running

    # Stop the bot and userbot gracefully
    await app.stop()
    await userbot.stop()

    # Log a closing message
    LOGGER("AnonXMusic").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝐂𝐡𝐢𝐧𝐧𝐚 ♨️\n╚═════ஜ۩۞۩ஜ════╝")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
