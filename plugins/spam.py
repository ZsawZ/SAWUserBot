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

@Client.on_message(filters.command("spam", prefixes=prefix) & filters.me)
async def spam(client: Client, message: Message):
        if not message.text.split("." + "spam", maxsplit=1)[1]:
                await message.edit("<i>Нету аргументов.</i>")
                return
        count = message.command[1]
        text = " ".join(message.command[2:])
        count = int(count)
        await message.delete()

        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Запущен спам"
        await Client.send_message("sawUSERBOT_LOGGERbot", log)

        for _ in range(count):
                await Client.send_message(message.chat.id, text)
                await asyncio.sleep(0.01)

module_list['Spam'] = f'{prefix}spam'
file_list['Spam'] = 'spam.py'