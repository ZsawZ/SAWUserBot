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

@Client.on_message(filters.command("drugs", prefixes=prefix) & filters.me)
async def drugs(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда drugs"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

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

module_list['Drugs'] = f'{prefix}drugs'
file_list['Drugs'] = 'drugs.py'