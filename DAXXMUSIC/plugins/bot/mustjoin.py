
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app

#--------------------------

MUST_JOIN = "ah07v"
#------------------------
@app.on_message(filters.incoming & filters.group, group=-1)
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://te.legra.ph/file/ba9d2c3c527ae4d01709a.jpg", caption=f"︙عـذراً، عـلـيـڪ الانـضـمـام الى هـذهِ الـقـنـاة أولاً  [ ♚...« مـكـنـوناتي 𝙷𝙼𝙳 »... ♚ ]({link}) \n︙اشـتـرڪ ثـم أرسـل : /start",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("♚...« مـكـنـوناتي 𝙷𝙼𝙳 »... ♚", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ارفع البوت مشࢪف في القناة: {MUST_JOIN} !")
