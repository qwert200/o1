from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatType
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app
from config import BANNED_USERS, lyrical

#--------------------------
MUST_JOIN = "ah07v"

async def subscription(_, __: Client, message: Message):
    try: await app.get_chat_member(MUST_JOIN, msg.from_user.id)
    except UserNotParticipant: return False
    return True

subscribed = filters.create(subscription)

@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("- ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ -", url=f"https://t.me/{MUST_JOIN}")]
    ])
    await message.reply(
        f"عذرًا عزيزي {user}عليك الإشتراك بقناة السورس أولا.",
        reply_markup = markup
    )
