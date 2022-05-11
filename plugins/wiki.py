@Client.on_message(filters.command("wiki", prefixes=prefix) & filters.me)

async def wiki(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Поиск в википедии"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    await message.edit("<b>Ищем инфу</b>")
    if user_request == "":
        wikipedia.set_lang("ru")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "en":
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f"""<b>Слово:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>""")
    except Exception as exc:
        await message.edit(f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>""")

module_list['Wikipedia'] = f'{prefix}wiki'
file_list['Wikipedia'] = 'wiki.py'