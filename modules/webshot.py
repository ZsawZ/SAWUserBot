@app.on_message(filters.command("webshot", prefixes=prefix) & filters.me)

async def webshot(client, message):

    try:
        if len(message.text.split()) < 2:
            await message.edit("<i>Нету аргументов.</i>")
            return
        user_link = message.command[1]
        await message.delete()
        full_link = "https://webshot.deam.io/{}/?width=1920&height=1080?type=png".format(user_link)
        await client.send_photo(message.chat.id, full_link, caption=f"<b> Ссылка ⟶ {user_link}</b>")


        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Скриншот сайта"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

    except:
        await message.edit("<i>Неизвестный сайт.</i>")
