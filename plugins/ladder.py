from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from time import time
from prefix import my_prefix
prefix = my_prefix()
from pyrogram.raw import functions, types
from pyrogram.types import Message, ChatPermissions
from pyrogram.utils import (
    get_channel_id,
    MAX_USER_ID,
    MIN_CHAT_ID,
    MAX_CHANNEL_ID,
    MIN_CHANNEL_ID,
)

@Client.on_message(filters.command("ladder", prefixes=prefix) & filters.me)
async def ladder(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Команда ladder"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    orig_text = message.text.split("." + "ladder ", maxsplit=1)[1]
    text = orig_text
    output = []
    for i in range(len(text) + 1):
     output.Clientend(text[:i])
    ot = "\n".join(output)
    await message.edit(ot)

module_list['Ladder'] = f'{prefix}ladder'
file_list['Ladder'] = 'ladder.py'