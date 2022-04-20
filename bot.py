#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, ChatSendMediaForbidden
from pyrogram.types import Message, ChatPermissions
from pyrogram.handlers import MessageHandler
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
from time import sleep, perf_counter, time
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import time, random, datetime, asyncio, sys, wikipedia, requests, json, colorama, requests, youtube_dl, subprocess, configparser
from gtts import gTTS
import os
import PIL
import re
from time import time
from typing import Dict, Union
from contextlib import suppress
import utils
from pyrogram import Client, ContinuePropagation, filters
from pyrogram.errors import (
    UserAdminInvalid,
    ChatAdminRequired,
    PeerIdInvalid,
    UsernameInvalid,
    RPCError,
)
from PIL import Image
from pyrogram.raw import functions, types
from pyrogram.types import Message, ChatPermissions
from pyrogram.utils import (
    get_channel_id,
    MAX_USER_ID,
    MIN_CHAT_ID,
    MAX_CHANNEL_ID,
    MIN_CHANNEL_ID,
)
import base64
from utils.scripts import with_reply, format_exc, resize_image
from io import BytesIO
import requests
from pyrogram import Client, filters, errors, types
from io import StringIO
from contextlib import redirect_stdout
from pyrogram import Client, filters
from pyrogram.types import Message


logo = """\033[31m
██████████████████████████████████████████████████████

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██████████▒▒▒▒▒▒█

█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██████████▒▒▄▀▒▒█

█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██████████▒▒▄▀▒▒█

█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██████████▒▒▄▀▒▒█

█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▒▒▒▒██▒▒▄▀▒▒█

█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█

█▒▒▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█

█████████▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒▒▒▄▀▒▒█

█▒▒▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▒▒█

█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒▒▒▄▀▒▒█

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒█

██████████████████████████████████████████████████████




██╗░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░░█████╗░████████╗

██║░░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗╚══██╔══╝

██║░░░██║╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██║░░██║░░░██║░░░

██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██║░░██║░░░██║░░░

╚██████╔╝██████╔╝███████╗██║░░██║░░░░░░██████╦╝╚█████╔╝░░░██║░░░

░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░
\033[34m
Telegram Канал - @SAWuser_bot
Помощь - @saw_andr
Версия 1.9.3 [СТАБИЛЬНАЯ]



Юзербот запущен!
Логи:"""
print(logo)

# Логи + Вход
app = Client("my_account")

logi = "╭ Логи\n┃ "

with app:
         app.join_chat("SAWuserbot") # Прошу, не убирайте эту строку

# Доп код перезагрузка
with app:
         app.unblock_user("sawUSERBOT_LOGGERbot")
         now = datetime.datetime.now()
         timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
         startlog = logi + timnow + "\n╰ Юзербот был запущен"
         app.send_message("sawUSERBOT_LOGGERbot", startlog)


         if len(sys.argv) == 4:
             try:
                 restart_type = sys.argv[3]
                 if restart_type == "1":
                    app.send_audio(sys.argv[1], "update.ogg", "<code>Обновление завершено!</code>")
                 else:
                    app.send_audio(sys.argv[1], "start.ogg", "<code>Перезагрузка завершена!</code>")
             except:
                pass

# Помощь | Инфа про Юзербота
@app.on_message(filters.command("help", prefixes=".") & filters.me)
async def help(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Список комманд"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("""<b><a href="https://t.me/SAWuserBot">🤖 UserBot SAW 1.9.3 [СТАБИЛЬНАЯ] 🤖</a></b>
<b><a href="https://t.me/sawandr">👨‍💻 Создатель 👨‍💻</a></b>
<b><a href="https://github.com/Brawl9008/SAWUserbot#readme">🤔 Как установить? 🤔</a></b>
<b><a href="https://telegra.ph/KOMANDY-SAWUSERBOT-04-17">📂 Команды 📂</a></b>""" ,disable_web_page_preview=True)

async def restart(message: Message, restart_type):
    if restart_type == "update": text = "1"
    else: text = "2"
    await os.execvp("python", ["python", "bot.py", f"{message.chat.id}",  f" {message.message_id}", f"{text}"])

@app.on_message(filters.command("restart", prefixes=".") & filters.me)
async def restartt(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был выключен"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.delete()
    await app.send_audio(message.chat.id, "stop.ogg", "<code>Перезагрузка...</code>")
    await restart(message, restart_type="restart")

@app.on_message(filters.command("update", prefixes=".") & filters.me)
async def update(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был обновлён"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("<code>Обновление...</code>")
    subprocess.call(["bash", "update.sh"])
    await message.edit("<code>Юзербот успешно обновлён!</code>")
    await restart(message, restart_type="update")

@app.on_message(filters.command("beta", prefixes=".") & filters.me)
async def beta(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был обновлён [СТАБИЛЬНАЯ]"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("<code>Обновление на СТАБИЛЬНУЮ версию...</code>")
    os.remove("bot.py")
    url = "https://raw.githubusercontent.com/Brawl9008/SAWUserbot/beta/bot.py"
    wget.download(url, "")
    await restart(message, restart_type="update")

# Префикс
@app.on_message(filters.command("sp", prefixes=".") & filters.me)
async def pref(client: Client, message: Message):
    if len(message.command) > 1:
        prefix = message.command[1]

        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Префикс был сменён на [ " + message.command[1] + " ]"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

        print(message.command)
        config.set("prefix", "prefix", prefixes=".")
        with open(config_path, "w") as config_file:
            config.write(config_file)
        await message.edit(f"<b>Префикс [ <code>{prefix}</code> ] установлен!</b>\nПожалуйста, подождите окончания перезагрузки")
        await restart(message, restart_type="restart")
    else:
        await message.edit("<b>Префикс не должен быть пустым!</b>")

# Репутация
@app.on_message(filters.text & filters.incoming & filters.regex("^\-$") & filters.reply)
async def repMinus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:

            now = datetime.datetime.now()
            timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
            l0g = logi + timnow + "\n╰ Репутация была понижена\n\n"

            with open("rep.txt", "r+") as f:
                data = f.read()
                data = int(data)
                num = 1
                rep = data - num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "💔 Вы понизили мою репутацию 💔\n🔝 Репутация " + str(repo) + " 🔝"
                await message.reply_text(text)
            log = l0g + "💔 Вы понизили мою репутацию 💔\n🔝 Репутация " + str(repo) + " 🔝"
            await app.send_message("sawUSERBOT_LOGGERbot", log)
    except:
        pass

@app.on_message(filters.text & filters.incoming & filters.regex("^\+$") & filters.reply)
async def repPlus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:

            now = datetime.datetime.now()
            timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
            l0g = logi + timnow + "\n╰ Репутация была повышена\n\n"

            with open("rep.txt", "r+") as f:
                data = f.read()
                data = int(data)
                num = 1
                rep = data + num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "❤️ Вы повысили мою репутацию ❤️\n🔝 Репутация " + str(repo) + " 🔝"
                await message.reply_text(text)
            log = l0g + "❤️ Вы повысили мою репутацию ❤️\n🔝 Репутация " + str(repo) + " 🔝"
            await app.send_message("sawUSERBOT_LOGGERbot", log)
    except:
        pass

# Айди
@app.on_message(filters.command("id", prefixes=".") & filters.me)
async def id(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда id"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if message.reply_to_message is None:
        await message.edit(f"Айди: {message.chat.id}")
    else:
        id = f"Айди: {message.reply_to_message.from_user.id}\nАйди чата: {message.chat.id}"
        await message.edit(id)

# Бомбер
@app.on_message(filters.command("bomber", prefixes=".") & filters.me)
async def b0mb3r(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запущен бомбер"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Запускаем бомбер")
    global bombe
    print("""
 _____                 _               
|  _  |               | |              
| |_) | ___  _ __ ___ | |__   ___ _ __ 
|  _ < / _ \| "_ ` _ \| "_ \ / _ \ "__|
| |_) | (_) | | | | | | |_) |  __/ |   
|____/ \___/|_| |_| |_|_.__/ \___|_|   
""")

    bombe = subprocess.Popen(["bomber"], stdout=subprocess.PIPE)
    await asyncio.sleep(5)
    await message.edit("Бомбер запущен!(неактуальный, плохо работает)\nСсылка: 127.0.0.1:8080")

@app.on_message(filters.command("sbomber", prefixes=".") & filters.me)
async def sbomber(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Бомбер выключен"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    bombe.terminate()
    await message.edit("Бомбер завершил свою роботу...")

@app.on_message(filters.command("bbomber", prefixes=".") & filters.me)
async def bbomber(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ bbomber включён"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    bomber = message.command[1]
    await app.send_message("BomberFree_bot", "/start")
    await app.send_message("couldboombot", "/start")
    await app.send_message("TNT_Robot", "/start")
    await message.edit("Запуск ботов")
    await asyncio.sleep(2)
    await app.send_message("couldboombot", "⚡️Запустить Spam")
    await app.send_message("TNT_Robot", "🧨 Бомбить")
    await asyncio.sleep(2)
    await app.send_message("BomberFree_bot", bomber)
    await app.send_message("couldboombot", bomber)
    await app.send_message("TNT_Robot", bomber + " 15")
    result = "Бомбер запущен на номер " + message.command[1]
    await message.edit(result)

# Время
@app.on_message(filters.command("time", prefixes=".") & filters.me)
async def time(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("%d.%m.%Y\nВремя %H:%M:%S")
    timenow = "Текущая дата : " + timnow
    await message.edit(timenow)

# Читы репутация
@app.on_message(filters.command("rep", prefixes=".") & filters.me)
async def repNakrutka(client: Client, message: Message):
    try:
        with open("rep.txt", "r+") as f:
            data = f.read()
            data = int(data)
            num = message.command[1]
            rep = num
            repo = str(rep)
            f.close()
        with open("rep.txt", "w+") as f:
            repo = str(rep)
            f.write(repo)
            f.close()
            text = "❤️ Репутация изменена ❤️\n🔝 Репутация " + str(repo) + " 🔝"
            await message.edit(text)

        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Накручена репутация\n\n❤️ Репутация изменена ❤️\n🔝 Репутация " + str(repo) + " 🔝"
        await app.send_message("sawUSERBOT_LOGGERbot", log)
    except:
        pass

# Спам
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam(client: Client, message: Message):
        if not message.text.split("." + "spam", maxsplit=1)[1]:
                await message.edit("<i>Нету аргументов.</i>")
                return
        count = message.command[1]
        text = " ".join(message.command[2:])
        count = int(count)
        await message.delete()

        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Запущен спам"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

        for _ in range(count):
                await app.send_message(message.chat.id, text)
                await asyncio.sleep(0.01)

# Скриншот сайта
@app.on_message(filters.command("webshot", prefixes=".") & filters.me)
async def webshot(client, message):
    try:
        if len(message.text.split()) < 2:
            await message.edit("<i>Нету аргументов.</i>")
            return
        user_link = message.command[1]
        await message.delete()
        full_link = "https://webshot.deam.io/{}/?width=1920&height=1080?type=png".format(user_link)
        await client.send_photo(message.chat.id, full_link, caption=f"<b> Ссылка ⟶ {user_link}</b>")


        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Скриншот сайта"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

    except:
        await message.edit("<i>Неизвестный сайт.</i>")

# Видео с ютуб
@app.on_message(filters.command("yt", prefixes=".") & filters.me)
async def yt(client, message):
    linked = message.command[1]

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на скачивания видео"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Скачивание видео...")
    ydl_opts = { "outtmpl": "video.mp4", }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([linked])
    await message.edit("Отправка видео...")
    await client.send_video(chat_id=message.chat.id, video="video.mp4", caption="Оригинал: " + message.command[1])
    await message.delete()
    os.remove("video.mp4")

@app.on_message(filters.command("myt", prefixes=".") & filters.me)
async def myt(client, message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на скачивание звука"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    myth = "youtube-dl -f 140 " + message.command[1] + " -o music.m4a"
    await message.edit("Скачивание аудиодорожки...")
    os.system(myth)
    await message.edit("Отправка аудиодорожки...")
    await client.send_audio(chat_id=message.chat.id, audio="music.m4a", caption="Звук с видео: " + message.command[1])
    await message.delete()
    os.remove("music.m4a")

# Призыв всех
@app.on_message(filters.command("tagall", prefixes=".") & filters.me)
async def tagall(client, message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Отмечены все участники"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

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

# Удалить смс
@app.on_message(filters.command("del", prefixes=".") & filters.me)
async def delete_messages(client: Client, message: Message):
    if message.reply_to_message:
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Удалено сообщение"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

        message_id = message.reply_to_message.message_id
        await message.delete()
        await client.delete_messages(message.chat.id, message_id)

# Пурдж
@app.on_message(filters.command("purge", prefixes=".") & filters.me)
async def purge(client: Client, message: Message):
        if message.reply_to_message:

                timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
                log = logi + timnow + "\n╰ Удаление всех сообщений"
                await app.send_message("sawUSERBOT_LOGGERbot", log)

                r = message.reply_to_message.message_id
                m = message.message_id
                msgs = []
                await message.delete()
                v = m - r
                while r != m:
                        msgs.append(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                r = message.reply_to_message.message_id
                msgs = []
                while r != m:
                        msgs.append(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                await app.send_message(message.chat.id, f"<b>Удалено > {v} сообщений!</b>")
        else:
                await message.edit("<i>А где реплай?</i>")

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
async def type(client: Client, message: Message):
    
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Коммада type"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    orig_text = message.text.split("." + "type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            await asyncio.sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            await asyncio.sleep(0.10)
        except FloodWait as e:
            await asyncio.sleep(e.x)

# Лестница
@app.on_message(filters.command("ladder", prefixes=".") & filters.me)
async def ladder(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда ladder"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    orig_text = message.text.split("." + "ladder ", maxsplit=1)[1]
    text = orig_text
    output = []
    for i in range(len(text) + 1):
     output.append(text[:i])
    ot = "\n".join(output)
    await message.edit(ot)

# Quotes
@app.on_message(filters.command("q", ".") & filters.me)
@with_reply
async def quote_cmd(client: Client, message: types.Message):
    if len(message.command) > 1 and message.command[1].isdigit():
        count = int(message.command[1])
        if count < 1:
            count = 1
        elif count > 15:
            count = 15
    else:
        count = 1

    is_png = "!png" in message.command or "!file" in message.command
    send_for_me = "!me" in message.command or "!ls" in message.command
    no_reply = "!noreply" in message.command or "!nr" in message.command

    messages = []

    async for msg in client.iter_history(
        message.chat.id, offset_id=message.reply_to_message.message_id, reverse=True
    ):
        if msg.empty:
            continue
        if msg.message_id >= message.message_id:
            break
        if no_reply:
            msg.reply_to_message = None

        messages.append(msg)

        if len(messages) >= count:
            break

    if send_for_me:
        await message.delete()
        message = await client.send_message("me", "<b>Generating...</b>")
    else:
        await message.edit("<b>Generating...</b>")

    url = "https://quotes.fl1yd.su/generate"
    params = {
        "messages": [
            await render_message(client, msg) for msg in messages if not msg.empty
        ],
        "quote_color": "#162330",
        "text_color": "#fff",
    }

    response = requests.post(url, json=params)
    if not response.ok:
        return await message.edit(
            f"<b>Quotes API error!</b>\n" f"<code>{response.text}</code>"
        )

    resized = resize_image(
        BytesIO(response.content), img_type="PNG" if is_png else "WEBP"
    )
    await message.edit("<b>Sending...</b>")

    try:
        func = client.send_document if is_png else client.send_sticker
        chat_id = "me" if send_for_me else message.chat.id
        await func(chat_id, resized)
    except errors.RPCError as e:  # no rights to send stickers, etc
        await message.edit(format_exc(e))
    else:
        await message.delete()


@app.on_message(filters.command("fq", ".") & filters.me)
@with_reply
async def fake_quote_cmd(client: Client, message: types.Message):
    is_png = "!png" in message.command or "!file" in message.command
    send_for_me = "!me" in message.command or "!ls" in message.command
    no_reply = "!noreply" in message.command or "!nr" in message.command

    fake_quote_text = " ".join(
        [
            arg
            for arg in message.command[1:]
            if arg not in ["!png", "!file", "!me", "!ls", "!noreply", "!nr"]
        ]  # remove some special arg words
    )

    if not fake_quote_text:
        return await message.edit("<b>Fake quote text is empty</b>")

    q_message = await client.get_messages(
        message.chat.id, message.reply_to_message.message_id
    )
    q_message.text = fake_quote_text
    q_message.entities = None
    if no_reply:
        q_message.reply_to_message = None

    if send_for_me:
        await message.delete()
        message = await client.send_message("me", "<b>Generating...</b>")
    else:
        await message.edit("<b>Generating...</b>")

    url = "https://quotes.fl1yd.su/generate"
    params = {
        "messages": [await render_message(client, q_message)],
        "quote_color": "#162330",
        "text_color": "#fff",
    }

    response = requests.post(url, json=params)
    if not response.ok:
        return await message.edit(
            f"<b>Quotes API error!</b>\n" f"<code>{response.text}</code>"
        )

    resized = resize_image(
        BytesIO(response.content), img_type="PNG" if is_png else "WEBP"
    )
    await message.edit("<b>Sending...</b>")

    try:
        func = client.send_document if is_png else client.send_sticker
        chat_id = "me" if send_for_me else message.chat.id
        await func(chat_id, resized)
    except errors.RPCError as e:  # no rights to send stickers, etc
        await message.edit(format_exc(e))
    else:
        await message.delete()


files_cache = {}


async def render_message(app: Client, message: types.Message) -> dict:
    async def get_file(file_id) -> str:
        if file_id in files_cache:
            return files_cache[file_id]

        file_name = await app.download_media(file_id)
        with open(file_name, "rb") as f:
            content = f.read()
        os.remove(file_name)
        data = base64.b64encode(content).decode()
        files_cache[file_id] = data
        return data

    # text
    if message.photo:
        text = message.caption if message.caption else ""
    elif message.poll:
        text = get_poll_text(message.poll)
    elif message.sticker:
        text = ""
    else:
        text = get_reply_text(message)

    # media
    if message.photo:
        media = await get_file(message.photo.file_id)
    elif message.sticker:
        media = await get_file(message.sticker.file_id)
    else:
        media = ""

    # entities
    entities = []
    if message.entities:
        for entity in message.entities:
            entities.append(
                {
                    "offset": entity.offset,
                    "length": entity.length,
                    "type": entity.type,
                }
            )

    def move_forwards(msg: types.Message):
        if msg.forward_from:
            msg.from_user = msg.forward_from
        if msg.forward_sender_name:
            msg.from_user.id = 0
            msg.from_user.first_name = msg.forward_sender_name
            msg.from_user.last_name = ""
        if msg.forward_from_chat:
            msg.sender_chat = msg.forward_from_chat
            msg.from_user.id = 0
        if msg.forward_signature:
            msg.author_signature = msg.forward_signature

    move_forwards(message)

    # author
    author = {}
    if message.from_user and message.from_user.id != 0:
        from_user = message.from_user

        author["id"] = from_user.id
        author["name"] = get_full_name(from_user)
        if message.author_signature:
            author["rank"] = message.author_signature
        elif message.chat.type != "supergroup" or message.forward_date:
            author["rank"] = ""
        else:
            try:
                member = await message.chat.get_member(from_user.id)
            except errors.UserNotParticipant:
                author["rank"] = ""
            else:
                author["rank"] = getattr(member, "title", "") or (
                    "owner"
                    if member.status == "creator"
                    else "admin"
                    if member.status == "administrator"
                    else ""
                )

        if from_user.photo:
            author["avatar"] = await get_file(from_user.photo.big_file_id)
        elif not from_user.photo and from_user.username:
            # may be user blocked us, we will try to get avatar via t.me
            t_me_page = requests.get(f"https://t.me/{from_user.username}").text
            sub = '<meta property="og:image" content='
            index = t_me_page.find(sub)
            if index != -1:
                link = t_me_page[index + 35 :].split('"')
                if (
                    len(link) > 0
                    and link[0]
                    and link[0] != "https://telegram.org/img/t_logo.png"
                ):
                    # found valid link
                    avatar = requests.get(link[0]).content
                    author["avatar"] = base64.b64encode(avatar).decode()
                else:
                    author["avatar"] = ""
            else:
                author["avatar"] = ""
        else:
            author["avatar"] = ""
    elif message.from_user and message.from_user.id == 0:
        author["id"] = 0
        author["name"] = message.from_user.first_name
        author["rank"] = ""
    else:
        author["id"] = message.sender_chat.id
        author["name"] = message.sender_chat.title
        author["rank"] = "channel" if message.sender_chat.type == "channel" else ""

        if message.sender_chat.photo:
            author["avatar"] = await get_file(message.sender_chat.photo.big_file_id)
        else:
            author["avatar"] = ""
    author["via_bot"] = message.via_bot.username if message.via_bot else ""

    # reply
    reply = {}
    reply_msg = message.reply_to_message
    if reply_msg and not reply_msg.empty:
        move_forwards(reply_msg)

        if reply_msg.from_user:
            reply["id"] = reply_msg.from_user.id
            reply["name"] = get_full_name(reply_msg.from_user)
        else:
            reply["id"] = reply_msg.sender_chat.id
            reply["name"] = reply_msg.sender_chat.title

        reply["text"] = get_reply_text(reply_msg)

    return {
        "text": text,
        "media": media,
        "entities": entities,
        "author": author,
        "reply": reply,
    }


def get_audio_text(audio: types.Audio) -> str:
    if audio.title and audio.performer:
        return f" ({audio.title} — {audio.performer})"
    elif audio.title:
        return f" ({audio.title})"
    elif audio.performer:
        return f" ({audio.performer})"
    else:
        return ""


def get_reply_text(reply: types.Message) -> str:
    return (
        "📷 Photo" + ("\n" + reply.caption if reply.caption else "")
        if reply.photo
        else get_reply_poll_text(reply.poll)
        if reply.poll
        else "📍 Location"
        if reply.location or reply.venue
        else "👤 Contact"
        if reply.contact
        else "🖼 GIF"
        if reply.animation
        else "🎧 Music" + get_audio_text(reply.audio)
        if reply.audio
        else "📹 Video"
        if reply.video
        else "📹 Videomessage"
        if reply.video_note
        else "🎵 Voice"
        if reply.voice
        else (reply.sticker.emoji + " " if reply.sticker.emoji else "") + "Sticker"
        if reply.sticker
        else "💾 File " + reply.document.file_name
        if reply.document
        else "🎮 Game"
        if reply.game
        else "🎮 set new record"
        if reply.game_high_score
        else f"{reply.dice.emoji} - {reply.dice.value}"
        if reply.dice
        else (
            "👤 joined the group"
            if reply.new_chat_members[0].id == reply.from_user.id
            else "👤 invited %s to the group"
            % (get_full_name(reply.new_chat_members[0]))
        )
        if reply.new_chat_members
        else (
            "👤 left the group"
            if reply.left_chat_member.id == reply.from_user.id
            else "👤 removed %s" % (get_full_name(reply.left_chat_member))
        )
        if reply.left_chat_member
        else f"✏ changed group name to {reply.new_chat_title}"
        if reply.new_chat_title
        else "🖼 changed group photo"
        if reply.new_chat_photo
        else "🖼 removed group photo"
        if reply.delete_chat_photo
        else "📍 pinned message"
        if reply.pinned_message
        else "🎤 started a new video chat"
        if reply.voice_chat_started
        else "🎤 ended the video chat"
        if reply.voice_chat_ended
        else "🎤 invited participants to the video chat"
        if reply.voice_chat_members_invited
        else "👥 created the group"
        if reply.group_chat_created or reply.supergroup_chat_created
        else "👥 created the channel"
        if reply.channel_chat_created
        else reply.text or "unsupported message"
    )


def get_poll_text(poll: types.Poll) -> str:
    text = get_reply_poll_text(poll) + "\n"

    text += poll.question + "\n"
    for option in poll.options:
        text += f"- {option.text}"
        if option.voter_count > 0:
            text += f" ({option.voter_count} voted)"
        text += "\n"

    text += f"Total: {poll.total_voter_count} voted"

    return text


def get_reply_poll_text(poll: types.Poll) -> str:
    if poll.is_anonymous:
        text = "📊 Anonymous poll" if poll.type == "regular" else "📊 Anonymous quiz"
    else:
        text = "📊 Poll" if poll.type == "regular" else "📊 Quiz"
    if poll.is_closed:
        text += " (closed)"

    return text


def get_full_name(user: types.User) -> str:
    name = user.first_name
    if user.last_name:
        name += " " + user.last_name
    return name

# ГС в текст
@app.on_message(filters.command("text", prefixes=".") & filters.me)
async def gstotext(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Ответь на сообщение")
        return

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Переведено голосовое в текст"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Пишу текстом...")
    await message.reply_to_message.forward("VoiceMsgBot")
    await asyncio.sleep(5)
    iii = await app.get_history("VoiceMsgBot")
    await message.edit("Отправка текста...")
    await app.forward_messages(message.chat.id, "VoiceMsgBot", iii[0].message_id)

# Ограничения
@app.on_message(filters.command("spamban", prefixes=".") & filters.me)
async def spamban(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Проверка нарушений"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Чекаю твой акк на наличие спамбана")
    await app.send_message("spambot", "/start")
    await asyncio.sleep(1)
    iii = await app.get_history("spambot")
    await message.delete()
    await app.forward_messages(message.chat.id, "spamBot", iii[0].message_id)

# Удаление всех с группы (200 уч лимит) !!! СКРЫТО
@app.on_message(filters.command("kickall hide", prefixes=".") & filters.me)
def kickall(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Удалены участники"
    app.send_message("sawUSERBOT_LOGGERbot", log)

    message.delete()
    num = 0
    for all in client.iter_chat_members(message.chat.id):
       try:
           num =+ 1
           client.kick_chat_member(message.chat.id, all.user.id, 0)
       except:
           pass

# Удаление всех с группы (200 уч лимит)
@app.on_message(filters.command("kickall", prefixes=".") & filters.me)
def kickall(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Удалены участники"
    app.send_message("sawUSERBOT_LOGGERbot", log)

    message.edit("Вашим участникам конец)")
    num = 0
    for all in client.iter_chat_members(message.chat.id):
       try:
           num =+ 1
           client.kick_chat_member(message.chat.id, all.user.id, 0)
       except:
           pass

@app.on_message(filters.command("infofull", prefixes=".") & filters.me)
async def info(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Полная информация"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

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

@app.on_message(filters.command("info", prefixes=".") & filters.me)
async def info(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Информация"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

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

# Пинг
@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Пинг"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    start = perf_counter()
    await message.edit("Измеряю пинг.")
    await message.edit("Измеряю пинг..")
    await message.edit("Измеряю пинг...")
    end = perf_counter()
    ping2 = end - start
    ping = ping2 * 1000

    if 0 <= ping <= 199:
        await message.edit(f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟢Качество соединение: Стабильное🟢")
    if 199 <= ping <= 400:
        await message.edit(f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟠Качество соединения: Хорошее🟠")
    if 400 <= ping <= 600:
        await message.edit(f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n🔴Качество соединения: Не стабильное🔴")
    if 600 <= ping:
        await message.edit(f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n⚠Качество соединения: Перепады связи⚠")

# Сократитель ссылок
linkToken = "6c2ac1846a1c1A2d5f88A3E5fbf0e14fcf96d7d0"
async def link_short(link: str):
    async with ClientSession(
        headers={
            "Authorization": f"API-Key {linkToken}"
        }
    ) as ses:
        async with ses.post(
            "https://api.waa.ai/v2/links",
            json={"url": link}
        ) as resp:
            return await resp.json()

@app.on_message(filters.command("short", prefixes=".") & filters.me)
async def shorten_link_command(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Сокращенная ссылка"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
         link = message.reply_to_message.text
    else:
        try:
            link = message.command[1]
        except IndexError:
            return await message.delete()
    output = (await link_short(link))["data"]
    await message.edit(f"Сокращенная ссылка: {output['link']}")

# QR-code
content_filter = filters.create(lambda _, __, msg: bool(get_cmd_content(msg)))

def get_cmd_content(message: Message):
    if message.reply_to_message:
        content = message.reply_to_message.text
    elif len(message.text.split(maxsplit=1)) == 2:
        content = message.text.split(maxsplit=1)[1]
    else:
        content = ""
    return content

@app.on_message(filters.command("qr", prefixes=".") & filters.me & content_filter)
async def qr_cmd(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Создан qr-code"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    text = get_cmd_content(message)
    await message.delete()
    async with ClientSession() as session:
        async with session.head("https://api.qrserver.com/v1/create-qr-code/", params={"data": text}) as resp:
            await app.send_photo(
                chat_id=message.chat.id,
                photo=str(resp.url),
                caption=text,
                parse_mode=None,
            )

# Википедия
@app.on_message(filters.command("wiki", prefixes=".") & filters.me)
async def wiki(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Поиск в википедии"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    await message.edit("<b>Ищем инфу</b>")
    if user_request == "":
        wikipedia.set_lang("ru")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "en":
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f"""<b>Слово:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>""")
    except Exception as exc:
        await message.edit(f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>""")

# Переклюяение раскладки
@app.on_message(filters.command("sw", prefixes=".") & filters.me)
async def switch(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда sw"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    text = " ".join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en_keys = """`qwertyuiop[]asdfghjkl;"zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
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

# Шифровка сообщений
@app.on_message(filters.command("cl", prefixes=".") & filters.me)
async def switch(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда cl"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

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

# Погода
def get_pic(city):
    file_name = f"{city}.png"
    with open(file_name, "wb") as pic:
        response = requests.get("http://wttr.in/{citys}_2&lang=ru.png", stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name

@app.on_message(filters.command("weather", prefixes=".") & filters.me)
async def weather(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Погода"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    city = message.command[1]
    await message.edit("```Загрузка...```")
    r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=ru")
    await message.edit(f"```City: {r.text}```")
    await client.send_photo(chat_id=message.chat.id, photo=get_pic(city), reply_to_message_id=message.message_id)
    os.remove(f"{city}.png")

# Поиск музыки
@app.on_message(filters.command("m", prefixes=".") & filters.me)
async def send_music(client: Client, message: Message):
    try:
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Поиск музыки"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

        cmd = message.command

        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            song_name = (
                message.reply_to_message.text or message.reply_to_message.caption
            )
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("Дай мне название музыки")
            await asyncio.sleep(2)
            await message.delete()
            return

        song_results = await app.get_inline_bot_results("deezermusicbot", song_name)

        try:
            # send to Saved Messages because hide_via doesn"t work sometimes
            saved = await app.send_inline_bot_result(
                chat_id="me",
                query_id=song_results.query_id,
                result_id=song_results.results[0].id,
                hide_via=True,
            )

            # forward as a new message from Saved Messages
            saved = await app.get_messages("me", int(saved.updates[1].message.id))
            reply_to = (
                message.reply_to_message.message_id
                if message.reply_to_message
                else None
            )
            await app.send_audio(
                chat_id=message.chat.id,
                audio=str(saved.audio.file_id),
                reply_to_message_id=reply_to,
            )

            # delete the message from Saved Messages
            await app.delete_messages("me", saved.message_id)
        except TimeoutError:
            await message.edit('That didn"t work out')
            await asyncio.sleep(2)
        await message.delete()
    except Exception as e:
        print(e)
        await message.edit("`Музыка не найденна`")
        await asyncio.sleep(2)
        await message.delete()

# Текст в речь
lang_code = os.environ.get("lang_code", "ru")

@app.on_message(filters.command("voice", prefixes=".") & filters.me)
async def voice(client, message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Текст в голосовое"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

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

# AFK
async def afk_handler(client: Client, message: Message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        if message.from_user.is_bot is False:
            await message.reply_text(f"<b>Я АФК уже {afk_time}</b>\n"
                                     f"<b>Причина:</b> <i>{reason}</i>")
    except NameError:
        pass

@app.on_message (filters.command("afk", prefixes=".") & filters.me)
async def afk(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Вход в АФК режим"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(MessageHandler(afk_handler, (filters.private & ~filters.me)))
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "Неизвестно"
    await message.edit(f"<b>Теперь я АФК</b>\n"
                       f"<b>Причина:</b> <i>{reason}</i>")

# No AFK
@app.on_message (filters.command("unafk", prefixes=".") & filters.me)
async def unafk(client: Client, message: Message):
    try:
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Выход с АФК режима"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        await message.edit(f"<b>Я теперь не АФК.\nБыл в афк {afk_time}</b>")
        client.remove_handler(*handler)
    except NameError:
        await message.edit("<b>Я не был в АФК</b>")
        await asyncio.sleep(3)
        await message.delete()

# Автоудаление сообщений
@app.on_message(filters.command("hide", prefixes=".") & filters.me)
async def hide(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Скрытие текста"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    orig_text = message.text.split("." + "hide ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            await asyncio.sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            await asyncio.sleep(0.10)
        except FloodWait as e:
            await asyncio.sleep(e.x)

    await asyncio.sleep(1.25)
    await message.delete()

# Авточтение
the_regex = r"^r\/([^\s\/])+"
f = filters.chat([])

@app.on_message(f)
async def auto_read(client: Client, message: Message):
    await app.read_history(message.chat.id)
    message.continue_propagation()

@app.on_message(filters.command("autoread", prefixes=".") & filters.me)
async def add_to_auto_read(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Авточтение"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Авточтение отключено")
    else:
        f.add(message.chat.id)
        await message.edit("Авточтение включено")

# Админ комманды
def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

def get_args(message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message  # Cannot split, let"s assume that it"s just one long message
    return list(filter(lambda x: len(x) > 0, split))

async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await app.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__Я не админ!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin or SELF.can_restrict_members:
            return True
        else:
            await message.edit("__недостаточно прав__")
            await asyncio.sleep(2)
            await message.delete()

@app.on_message(filters.command("leave", prefixes=".") & filters.me)
async def leave(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Выход с чата"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    m = await message.edit("<code>Всем пока... [Пользователь вышел с чата]</code>")
    await asyncio.sleep(2)
    await client.leave_chat(chat_id=message.chat.id)

@app.on_message(filters.command("ban", prefixes=".") & filters.me)
async def ban_command(client: Client, message: Message):
    cause = text(message)
    if message.reply_to_message and message.chat.type not in ["private", "channel"]:
        user_for_ban, name = await get_user_and_name(message)
        try:
            await client.ban_chat_member(message.chat.id, user_for_ban)
            channel = await client.resolve_peer(message.chat.id)
            user_id = await client.resolve_peer(user_for_ban)
            if "report_spam" in cause.lower().split():
                await client.send(
                    functions.channels.ReportSpam(
                        channel=channel,
                        participant=user_id,
                        id=[message.reply_to_message.message_id],
                    )
                )
            if "delete_history" in cause.lower().split():
                await client.send(
                    functions.channels.DeleteParticipantHistory(
                        channel=channel, participant=user_id
                    )
                )
            text_c = "".join(
                f" {_}"
                for _ in cause.split()
                if _.lower() not in ["delete_history", "report_spam"]
            )

            await message.edit(
                f"<b>{name}</b> <code>забанен!</code>"
                + f"\n{'<b>Cause:</b> <i>' + text_c.split(maxsplit=1)[1] + '</i>' if len(text_c.split()) > 1 else ''}"
            )
        except UserAdminInvalid:
            await message.edit("<b>Нет прав</b>")
        except ChatAdminRequired:
            await message.edit("<b>Нет прав</b>")
        except Exception as e:
            await message.edit(format_exc(e))
    elif not message.reply_to_message and message.chat.type not in [
        "private",
        "channel",
    ]:
        if len(cause.split()) > 1:
            try:
                if await check_username_or_id(cause.split(" ")[1]) == "channel":
                    user_to_ban = await client.get_chat(cause.split(" ")[1])
                elif await check_username_or_id(cause.split(" ")[1]) == "user":
                    user_to_ban = await client.get_users(cause.split(" ")[1])
                else:
                    await message.edit("<b>Человек не не найден</b>")
                    return

                name = (
                    user_to_ban.first_name
                    if getattr(user_to_ban, "first_name", None)
                    else user_to_ban.title
                )

                try:
                    channel = await client.resolve_peer(message.chat.id)
                    user_id = await client.resolve_peer(user_to_ban.id)
                    if (
                        "report_spam" in cause.lower().split()
                        and message.reply_to_message
                    ):
                        await client.send(
                            functions.channels.ReportSpam(
                                channel=channel,
                                participant=user_id,
                                id=[message.reply_to_message.message_id],
                            )
                        )
                    if "delete_history" in cause.lower().split():
                        await client.send(
                            functions.channels.DeleteParticipantHistory(
                                channel=channel, participant=user_id
                            )
                        )

                    text_c = "".join(
                        f" {_}"
                        for _ in cause.split()
                        if _.lower() not in ["delete_history", "report_spam"]
                    )

                    await client.ban_chat_member(message.chat.id, user_to_ban.id)
                    await message.edit(
                        f"<b>{name}</b> <code>забанен!</code>"
                        + f"\n{'<b>Cause:</b> <i>' + text_c.split(' ', maxsplit=2)[2] + '</i>' if len(text_c.split()) > 2 else ''}"
                    )
                except UserAdminInvalid:
                    await message.edit("<b>Нет прав</b>")
                except ChatAdminRequired:
                    await message.edit("<b>Нет прав</b>")
                except Exception as e:
                    await message.edit(format_exc(e))
            except PeerIdInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except UsernameInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except IndexError:
                await message.edit("<b>Пользователь не найден</b>")
        else:
            await message.edit("<b>айди или юзернейм/b>")
    else:
        await message.edit("<b>Unsupported</b>")

@app.on_message(filters.command("unban", prefixes=".") & filters.me)
async def unban_command(client: Client, message: Message):
    cause = text(message)
    if message.reply_to_message and message.chat.type not in ["private", "channel"]:
        user_for_unban, name = await get_user_and_name(message)
        try:
            await client.unban_chat_member(message.chat.id, user_for_unban)
            await message.edit(
                f"<b>{name}</b> <code>разбанен!</code>"
                + f"\n{'<b>Cause:</b> <i>' + cause.split(maxsplit=1)[1] + '</i>' if len(cause.split()) > 1 else ''}"
            )
        except UserAdminInvalid:
            await message.edit("<b>Нет прав</b>")
        except ChatAdminRequired:
            await message.edit("<b>Нет прав</b>")
        except Exception as e:
            await message.edit(format_exc(e))

    elif not message.reply_to_message and message.chat.type not in [
        "private",
        "channel",
    ]:
        if len(cause.split()) > 1:
            try:
                if await check_username_or_id(cause.split(" ")[1]) == "channel":
                    user_to_unban = await client.get_chat(cause.split(" ")[1])
                elif await check_username_or_id(cause.split(" ")[1]) == "user":
                    user_to_unban = await client.get_users(cause.split(" ")[1])
                else:
                    await message.edit("<b>Человек не найден!</b>")
                    return

                name = (
                    user_to_unban.first_name
                    if getattr(user_to_unban, "first_name", None)
                    else user_to_unban.title
                )

                try:
                    await client.unban_chat_member(message.chat.id, user_to_unban.id)
                    await message.edit(
                        f"<b>{name}</b> <code>разбанен!</code>"
                        + f"\n{'<b>Cause:</b> <i>' + cause.split(' ', maxsplit=2)[2] + '</i>' if len(cause.split()) > 2 else ''}"
                    )
                except UserAdminInvalid:
                    await message.edit("<b>Нет прав</b>")
                except ChatAdminRequired:
                    await message.edit("<b>Нет прав</b>")
                except Exception as e:
                    await message.edit(format_exc(e))
            except PeerIdInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except UsernameInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except IndexError:
                await message.edit("<b>Пользователь не найден</b>")
        else:
            await message.edit("<b>user_id or username</b>")
    else:
        await message.edit("<b>Unsupported</b>")

mute_permission = ChatPermissions(
    can_send_messages = False,
    can_send_media_messages = False,
    can_add_web_page_previews = False,
    can_send_polls = False,
    can_change_info = False,
    can_invite_users = False,
    can_pin_messages = False,
)

@app.on_message(filters.command("mute", prefixes=".") & filters.me)
async def mute_hammer(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на мут"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то замутить?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=mute_permission,
            )
            await message.edit(f"**{get_user.first_name} Был изолирован.**")
        except:
            await message.edit("**Я не могу замутить.**")
    else:
        await message.edit("**Я админ?**")

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@app.on_message(filters.command("unmute", prefixes=".") & filters.me)
async def unmute(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на размут"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то размутить?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=unmute_permissions,
            )
            await message.edit(f"**{get_user.first_name} Был размучен.**")
        except:
            await message.edit("**Я не могу размутить.**")
    else:
        await message.edit("**Я админ?**")

@app.on_message(filters.command("kick", prefixes=".") & filters.me)
async def kick_user(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на кик участника"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то кикнуть?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.kick_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
            )
            await message.edit(f"**Пользователь {get_user.first_name} был кикнут.**")
        except:
            await message.edit("**Я не могу кикать.**")
    else:
        await message.edit("**Я админ?**")

@app.on_message(filters.command("pin", prefixes=".") & filters.me)
async def pin_message(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на закрепление сообщения"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if message.chat.type in ["group", "supergroup"]:
        admins = await app.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await app.get_me()

        if me.id in admin_ids:
            if message.reply_to_message:
                disable_notification = True

                if len(message.command) >= 2 and message.command[1] in [
                    "alert",
                    "notify",
                    "loud",
                ]:
                    disable_notification = False

                await app.pin_chat_message(
                    message.chat.id,
                    message.reply_to_message.message_id,
                    disable_notification=disable_notification,
                )
                await message.edit("`Сообщение закрепленно!`")
            else:
                await message.edit(
                    "`Сделай ответ на сообщение`"
                )
        else:
            await message.edit("`Недостаточно прав`")
    else:
        await message.edit("`Я админ?`")
    await asyncio.sleep(3)
    await message.delete()

@app.on_message(filters.command("unpin", prefixes=".") & filters.me)
async def pin(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Сообщение закрепленно"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    try:
        message_id = message.reply_to_message.message_id
        await client.unpin_chat_message(message.chat.id, message_id)
        await message.edit("<code>Открепленно! </code>")
    except:
        await message.edit("<b>Сделайте реплай сообщению</b>")

@app.on_message(filters.command("admin", prefixes=".") & filters.me)
async def promote(client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Выдан статус админа одному из участников"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ.**")
        return
    title = "Admin"
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
        title = str(get_arg(message))
    else:
        args = get_args(message)
        if not args:
            await message.edit("**Я должен кого то повысить?**")
            return
        user = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(message.chat.id, user, can_pin_messages=True)
        if title == "":
            title = "Админ"
        await message.edit(
            f"**{get_user.first_name} Стал админом с званием [{title}]**"
        )
    except Exception as e:
        await message.edit(f"{e}")
    if title:
        try:
            await app.set_administrator_title(message.chat.id, user, title)
        except:
            pass

@app.on_message(filters.command("unadmin", prefixes=".") & filters.me)
async def demote(client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Отобран статус админа одному из участников"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ**")
        return
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я могу разжаловать админа?**")
            return
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(
            message.chat.id,
            user,
            is_anonymous=False,
            can_change_info=False,
            can_delete_messages=False,
            can_edit_messages=False,
            can_invite_users=False,
            can_promote_members=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_post_messages=False,
        )
        await message.edit(
            f"**{get_user.first_name} Больше не админ!**"
        )
    except Exception as e:
        await message.edit(f"{e}")

@app.on_message(filters.command("invite", prefixes=".") & filters.me)
async def invite(client, message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Участник приглашён"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я должен кого то пригласить?**")
            return
    get_user = await app.get_users(user)
    try:
        await app.add_chat_members(message.chat.id, get_user.id)
        await message.edit(f"**Пользователь {get_user.first_name} Был приглашён в этот чат!**")
    except Exception as e:
        await message.edit(f"{e}")

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
async def hack(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда hack"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    perc = 0
    while(perc < 100):
        try:
            text = "👮 Взлом пентагона в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Пентагон успешно взломан!"
    await message.edit(str(text))
    await asyncio.sleep(3)
    perc = 0
    while(perc < 100):
        try:
            text = "⬇️ Скачивание данных ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.15)
        except FloodWait as e:
            await asyncio.sleep(e.x)

    await asyncio.sleep(1)
    text = "🐓Нашли файлы что ты петух!"
    await message.edit(text)

# Команда Взлома жопы
@app.on_message(filters.command("jopa", prefixes=".") & filters.me)
async def jopa(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда jopa"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    perc = 0
    while(perc < 100):
        try:
            text = "🍑 Взлом жопы в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Жопа взломана"
    await message.edit(str(text))
    await asyncio.sleep(3)
    text = "🔍 Поиск Сливов ..."
    await message.edit(str(text))
    perc = 0
    await asyncio.sleep(3)
    while(perc < 100):
        try:
            text = "⬇️ Скачивание сливов ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 4)
            await asyncio.sleep(0.15)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Сливы были найдены"
    await message.edit(str(text))
    perc = 0
    await asyncio.sleep(5)
    while(perc < 100):
        try:
            text = "⬆️ Продажа сливов барыге..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.15)
        except FloodWait as e:
            await asyncio.sleep(e.x)

    text = "✅ Продано"
    await message.edit(str(text))
    await asyncio.sleep(2)
    rand =+ random.randint(100, 5000)
    bal = rand
    text = "💸 Вы заработали " + str(bal) + " ₽"
    await message.edit(text)

# Наркота
@app.on_message(filters.command("drugs", prefixes=".") & filters.me)
async def drugs(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда drugs"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    perc = 0
    result = 0
    while(perc < 100):
        try:
            text = "🍁Поиск запрещённых препаратов " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "Найдено 3 кг шпекса🍪💨"
    await message.edit(str(text))
    await asyncio.sleep(3)
    text = "Оформляем вкид 🌿⚗️"
    await message.edit(str(text))
    await asyncio.sleep(5)
    result += random.randint(1, 4)

    if result == 1:
        text = "🔥😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты 😳🔥"
        await message.edit(str(text))
    if result == 2:
        text = "🥴Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид🥴"
        await message.edit(str(text))
    if result == 3:
        text = "😖Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз😖"
        await message.edit(str(text))
    if result == 4:
        text = "😌Вы оформили вкид, Вам понравилось)😌"
        await message.edit(str(text))

# Оскорбление мамки
@app.on_message(filters.command("mum", prefixes=".") & filters.me)
async def mum(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда mum"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    text = "🔍 Поиск твоей мамки начался..."
    await message.edit(str(text))
    await asyncio.sleep(3.0)
    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Ищем твою мамашу на Авито... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.75)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "❌ Мамаша не найдена"
    await message.edit(str(text))
    await asyncio.sleep(3.0)

    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Поиск твоей мамаши на свалке... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.75)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "❌ Мамаша не найдена"
    await message.edit(str(text))

    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Поиск твоей мамки в канаве... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.75)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Мамка найдена... Она в канаве"
    await message.edit(str(text))



#shell
@app.on_message(filters.command("shell", prefixes=".") & filters.me)
async def shell(_, message: Message):
    if len(message.command) < 2:
        return await message.edit("<b>Specify the command in message text</b>")
    cmd_text = message.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "#" if os.getuid() == 0 else "$"
    text = f"<b>{char}</b> <code>{cmd_text}</code>\n\n"

    await message.edit(text + "<b>Running...</b>")
    try:
        start_time = perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "<b>Timeout expired (60 seconds)</b>"
    else:
        stop_time = perf_counter()
        if stdout:
            text += "<b>Output:</b>\n" f"<code>{stdout}</code>\n\n"
        if stderr:
            text += "<b>Error:</b>\n" f"<code>{stderr}</code>\n\n"
        text += f"<b>Completed in {round(stop_time - start_time, 5)} seconds with code {cmd_obj.returncode}</b>"
    await message.edit(text)
    cmd_obj.kill()
    
#demotivator
@app.on_message(filters.command("dem", prefixes=".") & filters.me)
async def demotivator(client, message):
    await message.edit("Создание демотиватора..")
 
    if message.reply_to_message.photo:
        await client.unblock_user("memegeneration_bot")
        capt = "1. " + message.text.split("." + "dem ", maxsplit=1)[1]
        await client.send_photo(
            chat_id="memegeneration_bot",
            photo=message.reply_to_message.photo.file_id,
        )
        photo = False
 
        while not photo:
            try:
                await asyncio.sleep(2)
                iii = await client.get_history("memegeneration_bot")
                await client.send_photo(chat_id=message.chat.id, photo=iii[0].photo.file_id)
                photo = True
                await message.delete()
            except:
                await asyncio.sleep(2)
    else:
        await message.edit("Сделайте реплай на фото")

@app.on_message(
    filters.command("exec", ".") & filters.me
)
def user_exec(client: Client, message: Message):
    if len(message.command) == 1:
        message.edit("<b>Code to execute isn't provided</b>")
        return

    reply = message.reply_to_message

    code = message.text.split(maxsplit=1)[1]
    stdout = StringIO()

    message.edit("<b>Executing...</b>")

    try:
        with redirect_stdout(stdout):
            exec(code)
        text = (
            "<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            "<b>Result</b>:\n"
            f"<code>{stdout.getvalue()}</code>"
        )
        if message.command[0] == "exnoedit":
            message.reply(text)
        else:
            message.edit(text)
    except Exception as e:
        message.edit(format_exc(e))


# noinspection PyUnusedLocal
@app.on_message(filters.command("eval", ".") & filters.me)
def user_eval(client: Client, message: Message):
    if len(message.command) == 1:
        message.edit("<b>Code to eval isn't provided</b>")
        return

    reply = message.reply_to_message

    code = message.text.split(maxsplit=1)[1]

    try:
        result = eval(code)
        message.edit(
            "<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            "<b>Result</b>:\n"
            f"<code>{result}</code>"
        )
    except Exception as e:
        message.edit(format_exc(e))

@app.run()
