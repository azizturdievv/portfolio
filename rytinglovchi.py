from pyrogram import Client, filters
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pyrogram import Client
from pyrogram.enums import ChatType
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")



app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

@app.on_message()
def get_channel_posts(client, message):
    channel_username = message.text.strip()
    try:
        # Kanalni olish
        channel = client.get_chat(channel_username)

        if channel.type == ChatType.CHANNEL:
            message.reply(f"Kanal topildi: {channel.title}. Postlarni tahlil qilaman...")

            # Kanal postlarini olish
            posts = list(client.get_chat_history(channel_username, limit=10))
            result = "Top 5 postlar:\n"

            for i, post in enumerate(posts[:5], start=1):
                views = post.views or 0
                reaction_count = 0

                # Reaktsiyalarni hisoblash
                if post.reactions:
                    try:
                        reaction_count = sum(
                            getattr(post.reactions, attr, 0)
                            for attr in dir(post.reactions)
                            if isinstance(getattr(post.reactions, attr, 0), int)
                        )
                    except:
                        reaction_count = 0  # Agar reaksiyalarni ololmasa, 0 qilamiz

                # Post linkini yaratish
                post_link = f"https://t.me/{channel_username.strip('@')}/{post.id}"
                result += f"{i}. [Post havolasi]({post_link}), Ko'rishlar: {views}, Reaksiyalar: {reaction_count}\n"

            message.reply(result, disable_web_page_preview=True)
        else:
            message.reply("Bu kanal emas. Iltimos, to'g'ri kanal nomini kiriting.")
    except Exception as e:
        message.reply(f"Xatolik yuz berdi: {str(e)}")

app.run()
