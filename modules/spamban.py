@app.on_message(filters.command("spamban", prefixes=prefix) & filters.me)

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