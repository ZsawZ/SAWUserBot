@app.on_message(filters.command("id", prefixes=prefix) & filters.me)

async def id(client: Client, message: Message):

    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда id"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    if message.reply_to_message is None:
        await message.edit(f"Айди: {message.chat.id}")
    else:
        id = f"Айди: {message.reply_to_message.from_user.id}\nАйди чата: {message.chat.id}"
        await message.edit(id)

module_list['id'] = f'{prefix}id'
file_list['id'] = 'id.py'