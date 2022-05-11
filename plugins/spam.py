@Client.on_message(filters.command("spam", prefixes=prefix) & filters.me)

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
        await Client.send_message("sawUSERBOT_LOGGERbot", log)

        for _ in range(count):
                await Client.send_message(message.chat.id, text)
                await asyncio.sleep(0.01)

module_list['Spam'] = f'{prefix}spam'
file_list['Spam'] = 'spam.py'