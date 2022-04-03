@Client.on_message(filters.command("infofull", prefixes=prefix) & filters.me)

async def info(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Полная информация"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
        last_name = message.reply_to_message.from_user.last_name
        number = message.reply_to_message.from_user.phone_number
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention
        last_name = message.from_user.last_name
        number = message.from_user.phone_number

    text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Фамилия: {last_name}
┃ Юзернейм: @{username}
┃ Номер телефонна: {number}
╰ Ссылка: {user_link}"""
    await message.edit(text, parse_mode="HTML")

@Client.on_message(filters.command("info", prefixes=prefix) & filters.me)
async def info(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Информация"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention

    text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Юзернейм: @{username}
╰ Ссылка: {user_link}"""
    await message.edit(text, parse_mode="HTML")

module_list['Whois'] = f'{prefix}info | {prefix}infofull | {prefix}bbomber'
file_list['Bomber'] = 'bomber.py'