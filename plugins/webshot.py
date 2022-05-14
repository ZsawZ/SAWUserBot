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

@Client.on_message(filters.command("webshot", prefixes=prefix) & filters.me)
async def webshot(client, message):
    try:
        if len(message.text.split()) < 2:
            await message.edit("<i>Нету аргументов.</i>")
            return
        user_link = message.command[1]
        await message.delete()
        full_link = "https://webshot.deam.io/{}/?width=1920&height=1080?type=png".format(user_link)
        await client.send_photo(message.chat.id, full_link, caption=f"<b> Ссылка ⟶ {user_link}</b>")


        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Скриншот сайта"
        await Client.send_message("sawUSERBOT_LOGGERbot", log)

    except:
        await message.edit("<i>Неизвестный сайт.</i>")

module_list['Webshot'] = f'{prefix}webshot'
file_list['Webshot'] = 'webshot.py'