@Client.on_message(filters.command("spamban", prefixes=prefix) & filters.me)

async def spamban(client: Client, message: Message):


    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Проверка нарушений"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Чекаю твой акк на наличие спамбана")
    await Client.send_message("spambot", "/start")
    await asyncio.sleep(1)
    iii = await Client.get_history("spambot")
    await message.delete()
    await Client.forward_messages(message.chat.id, "spamBot", iii[0].message_id)

module_list['Spamban'] = f'{prefix}spamban'
file_list['Bomber'] = 'bomber.py'