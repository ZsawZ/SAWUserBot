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

content_filter = filters.create(lambda _, __, msg: bool(get_cmd_content(msg)))
def get_cmd_content(message: Message):
    if message.reply_to_message:
        content = message.reply_to_message.text
    elif len(message.text.split(maxsplit=1)) == 2:
        content = message.text.split(maxsplit=1)[1]
    else:
        content = ""
    return content

@Client.on_message(filters.command("qr", prefixes=prefix) & filters.me & content_filter)
async def qr_cmd(client: Client, message: Message):
    text = get_cmd_content(message)
    await message.delete()
    async with ClientSession() as session:
        async with session.head("https://api.qrserver.com/v1/create-qr-code/", params={"data": text}) as resp:
            await Client.send_photo(
                chat_id=message.chat.id,
                photo=str(resp.url),
                caption=text,
                parse_mode=None,
            )

module_list['QRcode'] = f'{prefix}qr'
file_list['QRcode'] = 'qr.py'