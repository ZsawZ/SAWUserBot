@Client.on_message(filters.command("tagall", prefixes=prefix) & filters.me)

async def tagall(client, message):


    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Отмечены все участники"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    args = " ! "
    if len(message.text.split()) >= 2:
        args = message.text.split("." + "tagall ", maxsplit=1)[1]
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    members = client.iter_chat_members(chat_id)
    async for member in members:
        tag = member.user.username
        if limit <= 9:
            list = ["ᅠ", "ᅠ"]
            if tag != None:
                w = random.choice(list)
                string += f"<a href='https://t.me/{tag}'>{w}</a> "
            else:
                w = random.choice(list)
                string += f"<a href='tg://user?id={member.user.id}'>{w}</a> "
            limit += 1
        else:
            text = f"{args}|{string}"
            await client.send_message(chat_id, text, disable_web_page_preview=1)
            limit = 1
            string = ""
            await asyncio.sleep(2)

module_list['Tagall'] = f'{prefix}tagall'
file_list['Tagall'] = 'tagall.py'