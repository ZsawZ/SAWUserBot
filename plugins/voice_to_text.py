from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

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

@Client.on_message(filters.command("text", prefixes=prefix) & filters.me)
async def gstotext(client: Client, message: Message):

    if not message.reply_to_message:
        await message.edit("Ответь на сообщение")
        return
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Переведено голосовое в текст"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Пишу текстом...")
    await message.reply_to_message.forward("VoiceMsgBot")
    await asyncio.sleep(5)
    iii = await Client.get_history("VoiceMsgBot")
    await message.edit("Отправка текста...")
    await Client.forward_messages(message.chat.id, "VoiceMsgBot", iii[0].message_id)

module_list['Voice to text'] = f'{prefix}text'
file_list['Voice to text'] = 'voice_to_text.py'