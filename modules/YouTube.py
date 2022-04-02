@app.on_message(filters.command("yt", prefixes=prefix) & filters.me)

async def yt(client, message):

    linked = message.command[1]

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на скачивания видео"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("Скачивание видео...")
    ydl_opts = { "outtmpl": "video.mp4", }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([linked])
    await message.edit("Отправка видео...")
    await client.send_video(chat_id=message.chat.id, video="video.mp4", caption="Оригинал: " + message.command[1])
    await message.delete()
    os.remove("video.mp4")

@app.on_message(filters.command("myt", prefixes=".") & filters.me)
async def myt(client, message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на скачивание звука"
    await app.send_message("sawUSERBOT_LOGGERbot", log)

    myth = "youtube-dl -f 140 " + message.command[1] + " -o music.m4a"
    await message.edit("Скачивание аудиодорожки...")
    os.system(myth)
    await message.edit("Отправка аудиодорожки...")
    await client.send_audio(chat_id=message.chat.id, audio="music.m4a", caption="Звук с видео: " + message.command[1])
    await message.delete()
    os.remove("music.m4a")
