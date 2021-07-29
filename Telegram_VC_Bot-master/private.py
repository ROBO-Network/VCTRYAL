from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME,BOT_USERNAME
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/502a6d02cab5fa29595ce.jpg")
    await message.reply_text(
        f"""**Hey, I'm {BOT_NAME} 🎀
ι ϲᴀɴ ρʟᴀʏ мᴜѕɪᴄ ιɴ γᴏᴜʀ gʀᴏᴜᴩ νᴏɪᴄᴇ ϲʜᴀᴛ. ∂ᴇᴠᴇʟᴏᴩᴇᴅ ϐʏ  [AASTHA QUEEN 😇 𝘿𝙊𝙍𝙀𝙈𝙊𝙉 😇](https://t.me/itz_aastha_heartlessgirl) .
αᴅᴅ мᴇ τᴏ γᴏᴜʀ gʀᴏᴜᴩ αɴᴅ ρʟᴀʏ мᴜѕɪᴄ ƒʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐖𝐍𝐄𝐑😘", url="t.me/Mr_Robo_Official")
                  ],[
                    InlineKeyboardButton(
                        "𝐒𝐔𝐏𝐏𝐎𝐑𝐓👿", url="https://t.me/ROBO_Support"
                    ),
                    InlineKeyboardButton(
                        "𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="https://t.me/Robo_Network"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝐂𝐎  𝐎𝐖𝐍𝐄𝐑", url="https://t.me/Mr_Robo_Robot"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕𝐀𝐃𝐃 𝐓𝐎 𝐆𝐑𝐎𝐔𝐏➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aᴍ Oɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/Robo_Network")
                ]
            ]
        )
   )
