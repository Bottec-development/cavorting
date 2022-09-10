from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.bix_indificators import get_info
from keyboards.callback_datas import booking_callback


async def get_date_kb(office_type):
    date = await get_info(office_type)
    kb = InlineKeyboardMarkup()
    for i in date:
        btn = InlineKeyboardButton(text=f"{i} - {date[i][0]} ₽",callback_data=booking_callback.new(t="bxdate",o=i))
        kb.add(btn)
    return kb