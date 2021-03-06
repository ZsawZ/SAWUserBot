import os
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

lang_code = os.environ.get("lang_code", "ru")

@Client.on_message(filters.command("voice", prefixes=prefix) & filters.me)
async def voice(client, message):
    if len(message.text.split()) == 1:
        await message.edit(bantuan)
        return
    cust_lang = None
    await message.delete()
    await client.send_chat_action(message.chat.id, "record_audio")
    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang=lang_code)
    tts.save("voice.mp3")
    if message.reply_to_message:
        await client.send_voice(message.chat.id, voice="voice.mp3", reply_to_message_id=message.reply_to_message.message_id)
    else:
        await client.send_voice(message.chat.id, voice="voice.mp3")
    await client.send_chat_action(message.chat.id, action="cancel")
    os.remove("voice.mp3")

module_list['Text to voice'] = f'{prefix}voice'
file_list['Text to voice'] = 'text_to_voice.py'