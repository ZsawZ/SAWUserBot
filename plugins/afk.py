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

with app:
         app.unblock_user("sawUSERBOT_LOGGERbot")
         now = datetime.datetime.now()
         timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
         startlog = logi + timnow + "\n╰ Юзербот был запущен"
         app.send_message("sawUSERBOT_LOGGERbot", startlog)
logi = "╭ Логи\n┃ "

@Client.on_message (filters.command("afk", prefixes=prefix) & filters.me)
async def afk(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Вход в АФК режим"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(MessageHandler(afk_handler, (filters.private & ~filters.me)))
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "Неизвестно"
    await message.edit(f"<b>Теперь я АФК</b>\n"
                       f"<b>Причина:</b> <i>{reason}</i>")


@Client.on_message (filters.command("unafk", prefixes=prefix) & filters.me)
async def unafk(client: Client, message: Message):
    try:
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Выход с АФК режима"
        await Client.send_message("sawUSERBOT_LOGGERbot", log)

        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        await message.edit(f"<b>Я теперь не АФК.\nБыл в афк {afk_time}</b>")
        client.remove_handler(*handler)
    except NameError:
        await message.edit("<b>Я не был в АФК</b>")
        await asyncio.sleep(3)
        await message.delete()

module_list['Afk'] = f'{prefix}afk | {prefix}unafk'
file_list['Afk'] = 'afk.py'