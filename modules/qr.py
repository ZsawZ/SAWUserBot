content_filter = filters.create(lambda _, __, msg: bool(get_cmd_content(msg)))



def get_cmd_content(message: Message):
    if message.reply_to_message:
        content = message.reply_to_message.text
    elif len(message.text.split(maxsplit=1)) == 2:
        content = message.text.split(maxsplit=1)[1]
    else:
        content = ""
    return content

@Client.on_message(filters.command("qr", prefixes=prefix) & filters.me & content_filter)
async def qr_cmd(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Создан qr-code"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    text = get_cmd_content(message)
    await message.delete()
    async with ClientSession() as session:
        async with session.head("https://api.qrserver.com/v1/create-qr-code/", params={"data": text}) as resp:
            await Client.send_photo(
                chat_id=message.chat.id,
                photo=str(resp.url),
                caption=text,
                parse_mode=None,
            )

module_list['QRcode'] = f'{prefix}qr'
file_list['QR'] = 'bomber.py'