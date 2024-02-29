from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="‹ اوامر التشغيل ›", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="‹ طريقه التفعيل ›", callback_data="help_callback hb6"),
        ],
        [
            InlineKeyboardButton(text="‹ المطور ›", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="‹ قناة البوت ›", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="‹ اضف البوت لمجموعتك ›", url=f"https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons
