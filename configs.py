# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "7763257"))
	API_HASH = os.environ.get("API_HASH", "52c9cbf4b4ee78eda09eb3d9ac0673d7")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6185044354:AAGZbU6dU6SGtetcqCgR-KMlzE1PbBLmYvM")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "BeatzStoreBot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001987642974"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ThaniOruvan25:ThaniOruvan25@cluster0.cjv4s.mongodb.net/cluster0?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001584500398")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001861476160")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @AbirHasan2005

👥 **Support Group:** [Linux Repositories](https://t.me/DevsZone)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	HOME_TEXT2 = """
Dear [{}](tg://user?id={})

Welcome to @ViralBeatz Team ❤️. Thanks for Starting me.
"""
	HOME_TEXT0 = """
<code>Adding You In Database<\code>
"""
	HOME_TEXT1 = """
<code>Adding to @ViralBeatz Team ❤️.<\code>
"""
	HOME_TEXT3 = """
**I am a Advanced File Store Bot with some useful Tools ⚙.** 

	
