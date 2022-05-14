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

@Client.on_message(filters.command("purge", prefixes=prefix) & filters.me)
async def purge(client: Client, message: Message):
        if message.reply_to_message:

                timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
                log = logi + timnow + "\n╰ Удаление всех сообщений"
                await Client.send_message("sawUSERBOT_LOGGERbot", log)

                r = message.reply_to_message.message_id
                m = message.message_id
                msgs = []
                await message.delete()
                v = m - r
                while r != m:
                        msgs.Clientend(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                r = message.reply_to_message.message_id
                msgs = []
                while r != m:
                        msgs.Clientend(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                await Client.send_message(message.chat.id, f"<b>Удалено > {v} сообщений!</b>")
        else:
                await message.edit("<i>А где реплай?</i>")

module_list['Purge'] = f'{prefix}purge'
file_list['Purge'] = 'purge.py'