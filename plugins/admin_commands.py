from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

def get_arg(message):

    msg = message.text

    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

def get_args(message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message  # Cannot split, let"s assume that it"s just one long message
    return list(filter(lambda x: len(x) > 0, split))

async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await Client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__Я не админ!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin or SELF.can_restrict_members:
            return True
        else:
            await message.edit("__недостаточно прав__")
            await asyncio.sleep(2)
            await message.delete()

@Client.on_message(filters.command("leave", prefixes=prefix) & filters.me)
async def leave(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Выход с чата"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    m = await message.edit("<code>Всем пока... [Пользователь вышел с чата]</code>")
    await asyncio.sleep(2)
    await client.leave_chat(chat_id=message.chat.id)

@Client.on_message(filters.command("ban", prefixes=prefix) & filters.me)
async def ban_command(client: Client, message: Message):
    cause = text(message)
    if message.reply_to_message and message.chat.type not in ["private", "channel"]:
        user_for_ban, name = await get_user_and_name(message)
        try:
            await client.ban_chat_member(message.chat.id, user_for_ban)
            channel = await client.resolve_peer(message.chat.id)
            user_id = await client.resolve_peer(user_for_ban)
            if "report_spam" in cause.lower().split():
                await client.send(
                    functions.channels.ReportSpam(
                        channel=channel,
                        participant=user_id,
                        id=[message.reply_to_message.message_id],
                    )
                )
            if "delete_history" in cause.lower().split():
                await client.send(
                    functions.channels.DeleteParticipantHistory(
                        channel=channel, participant=user_id
                    )
                )
            text_c = "".join(
                f" {_}"
                for _ in cause.split()
                if _.lower() not in ["delete_history", "report_spam"]
            )

            await message.edit(
                f"<b>{name}</b> <code>забанен!</code>"
                + f"\n{'<b>Cause:</b> <i>' + text_c.split(maxsplit=1)[1] + '</i>' if len(text_c.split()) > 1 else ''}"
            )
        except UserAdminInvalid:
            await message.edit("<b>Нет прав</b>")
        except ChatAdminRequired:
            await message.edit("<b>Нет прав</b>")
        except Exception as e:
            await message.edit(format_exc(e))
    elif not message.reply_to_message and message.chat.type not in [
        "private",
        "channel",
    ]:
        if len(cause.split()) > 1:
            try:
                if await check_username_or_id(cause.split(" ")[1]) == "channel":
                    user_to_ban = await client.get_chat(cause.split(" ")[1])
                elif await check_username_or_id(cause.split(" ")[1]) == "user":
                    user_to_ban = await client.get_users(cause.split(" ")[1])
                else:
                    await message.edit("<b>Человек не не найден</b>")
                    return

                name = (
                    user_to_ban.first_name
                    if getattr(user_to_ban, "first_name", None)
                    else user_to_ban.title
                )

                try:
                    channel = await client.resolve_peer(message.chat.id)
                    user_id = await client.resolve_peer(user_to_ban.id)
                    if (
                        "report_spam" in cause.lower().split()
                        and message.reply_to_message
                    ):
                        await client.send(
                            functions.channels.ReportSpam(
                                channel=channel,
                                participant=user_id,
                                id=[message.reply_to_message.message_id],
                            )
                        )
                    if "delete_history" in cause.lower().split():
                        await client.send(
                            functions.channels.DeleteParticipantHistory(
                                channel=channel, participant=user_id
                            )
                        )

                    text_c = "".join(
                        f" {_}"
                        for _ in cause.split()
                        if _.lower() not in ["delete_history", "report_spam"]
                    )

                    await client.ban_chat_member(message.chat.id, user_to_ban.id)
                    await message.edit(
                        f"<b>{name}</b> <code>забанен!</code>"
                        + f"\n{'<b>Cause:</b> <i>' + text_c.split(' ', maxsplit=2)[2] + '</i>' if len(text_c.split()) > 2 else ''}"
                    )
                except UserAdminInvalid:
                    await message.edit("<b>Нет прав</b>")
                except ChatAdminRequired:
                    await message.edit("<b>Нет прав</b>")
                except Exception as e:
                    await message.edit(format_exc(e))
            except PeerIdInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except UsernameInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except IndexError:
                await message.edit("<b>Пользователь не найден</b>")
        else:
            await message.edit("<b>айди или юзернейм/b>")
    else:
        await message.edit("<b>Unsupported</b>")

@Client.on_message(filters.command("unban", prefixes=prefix) & filters.me)
async def unban_command(client: Client, message: Message):
    cause = text(message)
    if message.reply_to_message and message.chat.type not in ["private", "channel"]:
        user_for_unban, name = await get_user_and_name(message)
        try:
            await client.unban_chat_member(message.chat.id, user_for_unban)
            await message.edit(
                f"<b>{name}</b> <code>разбанен!</code>"
                + f"\n{'<b>Cause:</b> <i>' + cause.split(maxsplit=1)[1] + '</i>' if len(cause.split()) > 1 else ''}"
            )
        except UserAdminInvalid:
            await message.edit("<b>Нет прав</b>")
        except ChatAdminRequired:
            await message.edit("<b>Нет прав</b>")
        except Exception as e:
            await message.edit(format_exc(e))

    elif not message.reply_to_message and message.chat.type not in [
        "private",
        "channel",
    ]:
        if len(cause.split()) > 1:
            try:
                if await check_username_or_id(cause.split(" ")[1]) == "channel":
                    user_to_unban = await client.get_chat(cause.split(" ")[1])
                elif await check_username_or_id(cause.split(" ")[1]) == "user":
                    user_to_unban = await client.get_users(cause.split(" ")[1])
                else:
                    await message.edit("<b>Человек не найден!</b>")
                    return

                name = (
                    user_to_unban.first_name
                    if getattr(user_to_unban, "first_name", None)
                    else user_to_unban.title
                )

                try:
                    await client.unban_chat_member(message.chat.id, user_to_unban.id)
                    await message.edit(
                        f"<b>{name}</b> <code>разбанен!</code>"
                        + f"\n{'<b>Cause:</b> <i>' + cause.split(' ', maxsplit=2)[2] + '</i>' if len(cause.split()) > 2 else ''}"
                    )
                except UserAdminInvalid:
                    await message.edit("<b>Нет прав</b>")
                except ChatAdminRequired:
                    await message.edit("<b>Нет прав</b>")
                except Exception as e:
                    await message.edit(format_exc(e))
            except PeerIdInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except UsernameInvalid:
                await message.edit("<b>Пользователь не найден</b>")
            except IndexError:
                await message.edit("<b>Пользователь не найден</b>")
        else:
            await message.edit("<b>user_id or username</b>")
    else:
        await message.edit("<b>Unsupported</b>")

mute_permission = ChatPermissions(
    can_send_messages = False,
    can_send_media_messages = False,
    can_add_web_page_previews = False,
    can_send_polls = False,
    can_change_info = False,
    can_invite_users = False,
    can_pin_messages = False,
)

@Client.on_message(filters.command("mute", prefixes=prefix) & filters.me)
async def mute_hammer(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на мут"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то замутить?**")
                return
        try:
            get_user = await Client.get_users(user)
            await Client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=mute_permission,
            )
            await message.edit(f"**{get_user.first_name} Был изолирован.**")
        except:
            await message.edit("**Я не могу замутить.**")
    else:
        await message.edit("**Я админ?**")

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@Client.on_message(filters.command("unmute", prefixes=prefix) & filters.me)
async def unmute(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на размут"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то размутить?**")
                return
        try:
            get_user = await Client.get_users(user)
            await Client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=unmute_permissions,
            )
            await message.edit(f"**{get_user.first_name} Был размучен.**")
        except:
            await message.edit("**Я не могу размутить.**")
    else:
        await message.edit("**Я админ?**")

@Client.on_message(filters.command("kick", prefixes=prefix) & filters.me)
async def kick_user(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на кик участника"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то кикнуть?**")
                return
        try:
            get_user = await Client.get_users(user)
            await Client.kick_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
            )
            await message.edit(f"**Пользователь {get_user.first_name} был кикнут.**")
        except:
            await message.edit("**Я не могу кикать.**")
    else:
        await message.edit("**Я админ?**")

@Client.on_message(filters.command("pin", prefixes=prefix) & filters.me)
async def pin_message(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на закрепление сообщения"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if message.chat.type in ["group", "supergroup"]:
        admins = await Client.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await Client.get_me()

        if me.id in admin_ids:
            if message.reply_to_message:
                disable_notification = True

                if len(message.command) >= 2 and message.command[1] in [
                    "alert",
                    "notify",
                    "loud",
                ]:
                    disable_notification = False

                await Client.pin_chat_message(
                    message.chat.id,
                    message.reply_to_message.message_id,
                    disable_notification=disable_notification,
                )
                await message.edit("`Сообщение закрепленно!`")
            else:
                await message.edit(
                    "`Сделай ответ на сообщение`"
                )
        else:
            await message.edit("`Недостаточно прав`")
    else:
        await message.edit("`Я админ?`")
    await asyncio.sleep(3)
    await message.delete()

@Client.on_message(filters.command("unpin", prefixes=prefix) & filters.me)
async def pin(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Сообщение закрепленно"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    try:
        message_id = message.reply_to_message.message_id
        await client.unpin_chat_message(message.chat.id, message_id)
        await message.edit("<code>Открепленно! </code>")
    except:
        await message.edit("<b>Сделайте реплай сообщению</b>")

@Client.on_message(filters.command("admin", prefixes=prefix) & filters.me)
async def promote(client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Выдан статус админа одному из участников"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ.**")
        return
    title = "Admin"
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
        title = str(get_arg(message))
    else:
        args = get_args(message)
        if not args:
            await message.edit("**Я должен кого то повысить?**")
            return
        user = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
    get_user = await Client.get_users(user)
    try:
        await Client.promote_chat_member(message.chat.id, user, can_pin_messages=True)
        if title == "":
            title = "Админ"
        await message.edit(
            f"**{get_user.first_name} Стал админом с званием [{title}]**"
        )
    except Exception as e:
        await message.edit(f"{e}")
    if title:
        try:
            await Client.set_administrator_title(message.chat.id, user, title)
        except:
            pass

@Client.on_message(filters.command("unadmin", prefixes=prefix) & filters.me)
async def demote(client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Отобран статус админа одному из участников"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ**")
        return
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я могу разжаловать админа?**")
            return
    get_user = await Client.get_users(user)
    try:
        await Client.promote_chat_member(
            message.chat.id,
            user,
            is_anonymous=False,
            can_change_info=False,
            can_delete_messages=False,
            can_edit_messages=False,
            can_invite_users=False,
            can_promote_members=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_post_messages=False,
        )
        await message.edit(
            f"**{get_user.first_name} Больше не админ!**"
        )
    except Exception as e:
        await message.edit(f"{e}")

@Client.on_message(filters.command("invite", prefixes=prefix) & filters.me)
async def invite(client, message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Участник приглашён"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я должен кого то пригласить?**")
            return
    get_user = await Client.get_users(user)
    try:
        await Client.add_chat_members(message.chat.id, get_user.id)
        await message.edit(f"**Пользователь {get_user.first_name} Был приглашён в этот чат!**")
    except Exception as e:
        await message.edit(f"{e}")

module_list['Administrator'] = f'{prefix}leave | {prefix}ban | {prefix}unban | {prefix}mute | {prefix}unmute | {prefix}invite | {prefix}pin | {prefix}unpin | {prefix}admin | {prefix}unadmin | {prefix}kick'
file_list['Administrator'] = 'admin_commands.py'