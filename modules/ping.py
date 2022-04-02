@app.on_message(filters.command("ping", prefixes=prefix) & filters.me)

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
