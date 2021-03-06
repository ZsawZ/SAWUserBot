from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import time, random, datetime, asyncio, sys, wikipedia, requests, json, colorama, requests, youtube_dl, subprocess, configparser
from time import sleep, perf_counter, time

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
now = datetime.datetime.now()
timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")

@Client.on_message(filters.command("wiki", prefixes=prefix) & filters.me)
async def wiki(client: Client, message: Message):
    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    await message.edit("<b>Ищем инфу</b>")
    if user_request == "":
        wikipedia.set_lang("ru")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "en":
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f"""<b>Слово:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>""")
    except Exception as exc:
        await message.edit(f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>""")

module_list['Wikipedia'] = f'{prefix}wiki'
file_list['Wikipedia'] = 'wiki.py'