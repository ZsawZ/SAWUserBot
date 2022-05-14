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

@Client.on_message(filters.command("infofull", prefixes=prefix) & filters.me)
async def info(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Полная информация"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)
    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
        last_name = message.reply_to_message.from_user.last_name
        number = message.reply_to_message.from_user.phone_number
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention
        last_name = message.from_user.last_name
        number = message.from_user.phone_number

    text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Фамилия: {last_name}
┃ Юзернейм: @{username}
┃ Номер телефонна: {number}
╰ Ссылка: {user_link}"""
    await message.edit(text, parse_mode="HTML")

@Client.on_message(filters.command("info", prefixes=prefix) & filters.me)
async def info(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Информация"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention

    text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Юзернейм: @{username}
╰ Ссылка: {user_link}"""
    await message.edit(text, parse_mode="HTML")

module_list['Whois'] = f'{prefix}info | {prefix}infofull'
file_list['Whois'] = 'whois.py'