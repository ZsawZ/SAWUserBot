from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
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

@Client.on_message(filters.command("bomber", prefixes=prefix) & filters.me)
async def b0mb3r(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запущен бомбер"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

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

@Client.on_message(filters.command("sbomber", prefixes=prefix) & filters.me)
async def sbomber(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Бомбер выключен"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    bombe.terminate()
    await message.edit("Бомбер завершил свою роботу...")

@Client.on_message(filters.command("bbomber", prefixes=prefix) & filters.me)
async def bbomber(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ bbomber включён"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    bomber = message.command[1]
    await Client.send_message("BomberFree_bot", "/start")
    await Client.send_message("couldboombot", "/start")
    await Client.send_message("TNT_Robot", "/start")
    await message.edit("Запуск ботов")
    await asyncio.sleep(2)
    await Client.send_message("couldboombot", "⚡️Запустить Spam")
    await Client.send_message("TNT_Robot", "🧨 Бомбить")
    await asyncio.sleep(2)
    await Client.send_message("BomberFree_bot", bomber)
    await Client.send_message("couldboombot", bomber)
    await Client.send_message("TNT_Robot", bomber + " 15")
    result = "Бомбер запущен на номер " + message.command[1]
    await message.edit(result)

module_list['Bomber'] = f'{prefix}bomber | {prefix}sbomber | {prefix}bbomber'
file_list['Bomber'] = 'bomber.py'