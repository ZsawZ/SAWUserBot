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

@Client.on_message(filters.command("tagall", prefixes=prefix) & filters.me)
async def tagall(client, message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Отмечены все участники"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    args = " ! "
    if len(message.text.split()) >= 2:
        args = message.text.split("." + "tagall ", maxsplit=1)[1]
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    members = client.iter_chat_members(chat_id)
    async for member in members:
        tag = member.user.username
        if limit <= 9:
            list = ["ᅠ", "ᅠ"]
            if tag != None:
                w = random.choice(list)
                string += f"<a href='https://t.me/{tag}'>{w}</a> "
            else:
                w = random.choice(list)
                string += f"<a href='tg://user?id={member.user.id}'>{w}</a> "
            limit += 1
        else:
            text = f"{args}|{string}"
            await client.send_message(chat_id, text, disable_web_page_preview=1)
            limit = 1
            string = ""
            await asyncio.sleep(2)

module_list['Tagall'] = f'{prefix}tagall'
file_list['Tagall'] = 'tagall.py'