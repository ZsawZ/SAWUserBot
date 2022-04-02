@app.on_message(filters.command("type", prefixes=prefix) & filters.me)

async def type(client: Client, message: Message):

    
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Коммада type"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    orig_text = message.text.split("." + "type ", maxsplit=1)[1]
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
