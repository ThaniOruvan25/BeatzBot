from configs import Config
from handlers.database import db
from pyrogram import Client
from pyrogram.types import Message
async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"<b>#NewUser #{cmd.from_user.first_name} #{cmd.from_user.id}</b>\n\n"
                f"➺ Name: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n"
                f"➺ Tɢ Iᴅ: {cmd.from_user.id}\n\n"
                f"➺ Total Users: <code>{db.total_users_count()}</code>"
            )
            await bot.send_message(
                int(Config.TO_CHANNEL),
                f"<b>#NewUser #{cmd.from_user.first_name} #{cmd.from_user.id} #{Config.BOT_USERNAME}</b>\n\n"
                f"➺ Name: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n"
                f"➺ Tɢ Iᴅ: {cmd.from_user.id}\n\n"
                f"➺ Total Users: <code>{db.total_users_count()}</code>"
            )

