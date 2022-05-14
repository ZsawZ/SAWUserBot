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


@Client.on_message(filters.command("del", prefixes=prefix) & filters.me)
async def delete_messages(client: Client, message: Message):

    if message.reply_to_message:
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Удалено сообщение"
        await Client.send_message("sawUSERBOT_LOGGERbot", log)

        message_id = message.reply_to_message.message_id
        await message.delete()
        await client.delete_messages(message.chat.id, message_id)

module_list['Delete'] = f'{prefix}del'
file_list['Delete'] = 'del.py'