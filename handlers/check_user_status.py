# (c) Mr. Vishal & @AbirHasan2005

import datetime
from configs import Config
from handlers.database import Database

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)


async def handle_user_status(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        await bot.send_message(
            Config.LOG_CHANNEL,
            f"<b>#{cmd.from_user.first_name} #{cmd.from_user.id}\n\n➺Nᴀᴍᴇ - [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n➺Tɢ Iᴅ - {cmd.from_user.id}\n\n➺Tᴏᴛᴀʟ Uꜱᴇʀꜱ - <code>{db.total_users_count()}<\code></b>"
        )
        
        z = await bot.send_message(
            Config.TO_CHANNEL,
            f"<b>#{cmd.from_user.first_name} #{cmd.from_user.id} #{Config.BOT_USERNAME}\n\n➺Nᴀᴍᴇ - [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n➺Tɢ Iᴅ - {cmd.from_user.id}\n\n➺Tᴏᴛᴀʟ Uꜱᴇʀꜱ - <code>{db.total_users_count()}</code></b>"
            )
    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        await z.edit(f"<b>#{cmd.from_user.first_name} #{cmd.from_user.id} #{Config.BOT_USERNAME}\n\n➺Nᴀᴍᴇ - [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n➺Tɢ Iᴅ - {cmd.from_user.id}\n\n <i>This User is Banned.</i>➺Tᴏᴛᴀʟ Uꜱᴇʀꜱ - <code>{db.total_users_count()}</code></b>")
        if (datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("<b>ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ʙʏ ᴍʏ ᴀᴅᴍɪɴ! ᴄᴏɴᴛᴀᴄᴛ @ViralBeatzBot ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ.</b>", quote=True)
            return
    await cmd.continue_propagation()
