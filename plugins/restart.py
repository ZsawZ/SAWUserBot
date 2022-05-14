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

@Client.on_message(filters.command("restart", prefixes=prefix) & filters.me)
async def restartt(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был выключен"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.delete()
    await Client.send_audio(message.chat.id, "stop.ogg", "<code>Перезагрузка...</code>")
    await restart(message, restart_type="restart")

@Client.on_message(filters.command("update", prefixes=prefix) & filters.me)
async def updatte(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был обновлён"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("<code>Обновление...</code>")
    subprocess.call(["bash", "update.sh"])
    await message.edit("<code>Юзербот успешно обновлён!</code>")
    await restart(message, restart_type="1")

module_list['Restarter'] = f'{prefix}restart | {prefix}update'
file_list['Restarter'] = 'restart.py'