from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import time, random, datetime, asyncio, sys, wikipedia, requests, json, colorama, requests, youtube_dl, subprocess, configparser

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

@Client.on_message(filters.command("time", prefixes=prefix) & filters.me)
async def time(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("%d.%m.%Y\nВремя %H:%M:%S")
    timenow = "Текущая дата : " + timnow
    await message.edit(timenow)
    
module_list['Time'] = f'{prefix}time'
file_list['Time'] = 'time.py'