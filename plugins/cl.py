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

now = datetime.datetime.now()
timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")


@Client.on_message(filters.command("cl", prefixes=prefix) & filters.me)
async def switch(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда cl"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    text = " ".join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en_keys = """異體字体♬♝♞♟γδεηθκλμνZXM∩SάằẫăǽẳßβЂ฿™đďÐðӘҾΣĤĦҤḦĥћҥḧŒœØỢ$śşŝšṧṩᵴﮐ§♌♍♎♏♐♑♒♓✵✶✷✸✹"""
    if text == "":
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            await message.edit("Текст отсутствует")
            await asyncio.sleep(3)
            await message.delete()
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)

module_list['Cl'] = f'{prefix}cl'
file_list['Cl'] = 'cl.py'