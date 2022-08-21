from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def inforamtion_keyboard(latitude, longitude):
    kb = InlineKeyboardMarkup(row_width=2)
    phone = InlineKeyboardButton(text='Позвонить', callback_data=f'send_phone')
    taxi = InlineKeyboardButton(text='Вызвать такси',
                                url=f"https://taxi.yandex.ru/?utm_source&utm_medium&gto={latitude}%2C%20{longitude}")
    address = InlineKeyboardButton(text='Адрес', callback_data=f'send_address')
    back_to_menu = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'back_to_menu_callback')
    kb.row(phone, taxi)
    kb.row(address)
    kb.row(back_to_menu)
    return kb


async def back_to_information():
    kb = InlineKeyboardMarkup(row_width=1)
    to_information = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'information')
    kb.insert(to_information)
    return kb
