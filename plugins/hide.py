@Client.on_message(filters.command("hide", prefixes=prefix) & filters.me)
async def hide(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Скрытие текста"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    orig_text = message.text.split("." + "hide ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            await asyncio.sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            await asyncio.sleep(0.10)
        except FloodWait as e:
            await asyncio.sleep(e.x)

    await asyncio.sleep(1.25)
    await message.delete()

module_list['Hider'] = f'{prefix}hide'
file_list['Hider'] = 'hide.py'