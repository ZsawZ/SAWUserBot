from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
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
import time, random, datetime, asyncio, sys, wikipedia, requests, json, colorama, requests, youtube_dl, subprocess, configparser


the_regex = r"^r\/([^\s\/])+"
f = filters.chat([])

@Client.on_message(f)
async def auto_read(client: Client, message: Message):
    await Client.read_history(message.chat.id)
    message.continue_propagation()

@Client.on_message(filters.command("autoread", prefixes=prefix) & filters.me)
async def add_to_auto_read(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Авточтение"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Авточтение отключено")
    else:
        f.add(message.chat.id)
        await message.edit("Авточтение включено")

module_list['autoread'] = f'{prefix}autoread'
file_list['autoread'] = 'autoread.py'