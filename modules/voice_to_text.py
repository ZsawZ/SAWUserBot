@Client.on_message(filters.command("text", prefixes=prefix) & filters.me)

async def gstotext(client: Client, message: Message):

    if not message.reply_to_message:
        await message.edit("Ответь на сообщение")
        return

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Переведено голосовое в текст"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Пишу текстом...")
    await message.reply_to_message.forward("VoiceMsgBot")
    await asyncio.sleep(5)
    iii = await Client.get_history("VoiceMsgBot")
    await message.edit("Отправка текста...")
    await Client.forward_messages(message.chat.id, "VoiceMsgBot", iii[0].message_id)

module_list['Voice to text'] = f'{prefix}text'
file_list['Vo'] = 'bomber.py'