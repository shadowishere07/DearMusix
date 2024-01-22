import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app  

photo = [
    "https://telegra.ph/file/3ca0e53b5604943c1dcc9.jpg",
    "https://telegra.ph/file/24d9f14314ce58c6efa74.jpg",
    "https://telegra.ph/file/73844e707166f442ff3ef.jpg",
    "https://telegra.ph/file/71e1b11d1c8f881500a52.jpg",
    "https://telegra.ph/file/3fec5a206cc3f26031810.jpg",
    "https://telegra.ph/file/5772babff78ef614cd0fe.jpg",
    "https://telegra.ph/file/0dd688fa045e146bd0cba.jpg",
    "https://telegra.ph/file/09501679c7d395a6fef46.jpg",
    "https://telegra.ph/file/b32511341f9b8fa9ed51e.jpg",
    "https://telegra.ph/file/0f69cf467a814fa9edb96.jpg",
    "https://telegra.ph/file/57b886be48fce1f9fa20f.jpg",
    "https://telegra.ph/file/532197d0d4bd314c29d51.jpg,
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✍️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
