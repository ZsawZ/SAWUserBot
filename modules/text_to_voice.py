lang_code = os.environ.get("lang_code", "ru")



@Client.on_message(filters.command("voice", prefixes=prefix) & filters.me)
async def voice(client, message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Текст в голосовое"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if len(message.text.split()) == 1:
        await message.edit(bantuan)
        return
    cust_lang = None
    await message.delete()
    await client.send_chat_action(message.chat.id, "record_audio")
    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang=lang_code)
    tts.save("voice.mp3")
    if message.reply_to_message:
        await client.send_voice(message.chat.id, voice="voice.mp3", reply_to_message_id=message.reply_to_message.message_id)
    else:
        await client.send_voice(message.chat.id, voice="voice.mp3")
    await client.send_chat_action(message.chat.id, action="cancel")
    os.remove("voice.mp3")

module_list['Text to voice'] = f'{prefix}voice | {prefix}sbomber | {prefix}bbomber'
file_list['Bomber'] = 'bomber.py'