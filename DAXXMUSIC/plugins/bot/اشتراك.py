from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatType
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app
from config import BANNED_USERS, lyrical

#--------------------------


#------------------------
chid = "ah07v"


def main_mark():
    invite = bot.create_chat_invite_link(chid)
    InviteLink = invite.invite_link
    mrkplink = InlineKeyboardMarkup()
    mrkplink.add(InlineKeyboardButton("اشترك في قناة البوت لاستخدام الاوامر! 🚀", url=InviteLink))
    return mrkplink


def main(message:Message):
    user_id = message.from_user.id
    pr_id = message.chat.id
    div = myId == user_id
    try:
        request = bot.get_chat_member(chid, user_id).status
        List_ch = ['member', 'administrator, creator']
        if request in List_ch or div:
            bot.send_message(pr_id, "اهلا بك عزيزي, مرحبا بعودتك!")
        else:
            bot.send_message(pr_id, "اهلا بك عزيزي, اشترك في قناة البوت اولا!", reply_markup=main_mark())
    except:
        bot.send_message(pr_id,"البوت غير موجود في قناة الاشتراك!" )



    
