@Client.on_message(filters.command("hack", prefixes=prefix) & filters.me)

async def hack(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда hack"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

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

module_list['Pentagon'] = f'{prefix}hack'
file_list['Pentagon'] = 'hack.py'