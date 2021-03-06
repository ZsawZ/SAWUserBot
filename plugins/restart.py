import os
import zipfile
import wget
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
import subprocess
from prefix import my_prefix
prefix = my_prefix()


async def restart(message: Message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"
    try:
        await os.execvp(
            "python3",
            [
                "python3",
                "./main.py",
                f"{message.chat.id}",
                f"{message.message_id}",
                f"{text}",
            ],
        )
    except:
        await os.execvp(
            "python",
            [
                "python",
                "./main.py",
                f"{message.chat.id}",
                f"{message.message_id}",
                f"{text}",
            ],
        )


# Restart
@Client.on_message(filters.command("restart", prefixes=prefix) & filters.me)
async def restart_get(client, message):
    try:
        await message.edit("**Restarting userbot...**")
        await restart(message, restart_type="restart")
    except:
        await message.edit("**An error occured...**")


# Update
@Client.on_message(filters.command('update', prefixes=prefix) & filters.me)
async def update(client, message):
    try:
        await message.edit("<code>Обновление...</code>")
        subprocess.call(["bash", "update.sh"])
        await message.edit("<code>Юзербот успешно обновлён!</code>")
        await restart(message, restart_type="update")
    except:
        await message.edit("**An error occured...**")


module_list['Restarter'] = f'{prefix}update | {prefix}restart'
file_list['Restarter'] = 'restarter.py'
