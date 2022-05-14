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

@Client.on_message(filters.command("spamban", prefixes=prefix) & filters.me)
async def spamban(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Проверка нарушений"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Чекаю твой акк на наличие спамбана")
    await Client.send_message("spambot", "/start")
    await asyncio.sleep(1)
    iii = await Client.get_history("spambot")
    await message.delete()
    await Client.forward_messages(message.chat.id, "spamBot", iii[0].message_id)

module_list['Spamban'] = f'{prefix}spamban'
file_list['Spamban'] = 'spamban.py'