from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Gᴇɴᴇʀᴀᴛᴇ Sᴇssɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ | 🌛", url="https://t.me/PUNJABI_HINDI_CHAT"),
         InlineKeyboardButton("Mʀ. Dʜɪᴍᴀɴ | 🌛", url="https://t.me/I_DXLVIR"),
        ],
    ]

    START = """
Hᴇʏ {},
Tʜɪs ɪs {},
sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
Sᴏᴜʀᴄᴇ : [Cʟɪᴄᴋ Hᴇʀᴇ Tᴏ Gᴇᴛ](https://t.me/I_DXLVIR)
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [Dʜɪᴍᴀɴ](https://t.me/I_DXLVIR) !
    """
