the_regex = r"^r\/([^\s\/])+"
f = filters.chat([])

@Client.on_message(f)
async def auto_read(client: Client, message: Message):
    await Client.read_history(message.chat.id)
    message.continue_propagation()

@Client.on_message(filters.command("autoread", prefixes=prefix) & filters.me)
async def add_to_auto_read(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Авточтение"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Авточтение отключено")
    else:
        f.add(message.chat.id)
        await message.edit("Авточтение включено")

module_list['autoread'] = f'{prefix}autoread'
file_list['autoread'] = 'autoread.py'