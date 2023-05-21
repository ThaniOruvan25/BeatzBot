# (c) @AbirHasan2005

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
                f"<b>#NewUser #{cmd.from_user.first_name} #{cmd.from_user.id}\n\n➺Nᴀᴍᴇ - [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n➺Tɢ Iᴅ - {cmd.from_user.id}\n\n➺Tᴏᴛᴀʟ Uꜱᴇʀꜱ - <code>{db.total_users_count()}<\code><\b>"
            )
