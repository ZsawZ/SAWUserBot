@Client.on_message(filters.command("ladder", prefixes=prefix) & filters.me)

async def ladder(client: Client, message: Message):


    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Команда ladder"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    orig_text = message.text.split("." + "ladder ", maxsplit=1)[1]
    text = orig_text
    output = []
    for i in range(len(text) + 1):
     output.Clientend(text[:i])
    ot = "\n".join(output)
    await message.edit(ot)

module_list['Ladder'] = f'{prefix}ladder'
file_list['Ladder'] = 'ladder.py'