from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>Hai, saya adalah PikaStream_bot.</b>
"""

    HELP_TEXT = """
<b>Kirimkan file atau video dan dapatkan link stream dari file/video anda """

    ABOUT_TEXT = """
<b>Nama bot : {}</b>\n
<b>Versi : {}</b>
<b>Update : 06-January-2024</b>
<b>Maintainer : <a href='https://telegram.me/pikadotchu'>𝑷𝒊𝒌𝒂𝒄𝒉𝒖</a></b>\n
"""

    STREAM_TEXT = """
<b>📂 Nama File :</b> <b>{}</b>\n
<b>📦 Ukuran :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<b>📂 Nama File :</b> <b>{}</b>\n
<b>📦 Ukuran :</b> <code>{}</code>\n"""


    BAN_TEXT = "**Anda tidak diizinkan menggunakan bot ini**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Bantuan', callback_data='help'),
            InlineKeyboardButton('Tentang', callback_data='about'),
            InlineKeyboardButton('Tutup', callback_data='close')
        ],
            [InlineKeyboardButton("📢 Channel Update", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Bantuan', callback_data='help'),
            InlineKeyboardButton('Tentang', callback_data='about'),
            InlineKeyboardButton('Tutup', callback_data='close')
        ],
            [InlineKeyboardButton("📢 Channel Update", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Bantuan', callback_data='help'),
            InlineKeyboardButton('Tentang', callback_data='about'),
            InlineKeyboardButton('Tutup', callback_data='close')
        ],
            [InlineKeyboardButton("📢 Channel Update", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
