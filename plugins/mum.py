@Client.on_message(filters.command("mum", prefixes=prefix) & filters.me)

async def mum(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда mum"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

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

module_list['Mum'] = f'{prefix}mum'
file_list['Mum'] = 'mum.py'