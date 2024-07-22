from pyrogram import filters
from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import add_off, add_on
from AnonXMusic.utils.decorators.language import language

@app.on_message(filters.command(["logger"]) & SUDOERS)
@language
async def logger(client, message, _):
    # Usage message for incorrect command usage
    usage = _["log_1"]
    
    # Check if the command has exactly two arguments
    if len(message.command) != 2:
        return await message.reply_text(usage)
    
    # Get the state from the command arguments
    state = message.text.split(None, 1)[1].strip().lower()
    
    # Enable logging
    if state == "enable":
        await add_on(2)
        await message.reply_text(_["log_2"])
    
    # Disable logging
    elif state == "disable":
        await add_off(2)
        await message.reply_text(_["log_3"])
    
    # If the state is neither 'enable' nor 'disable', show the usage message
    else:
        await message.reply_text(usage)
