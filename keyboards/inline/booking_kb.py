from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def accept_booking_kb():
    kb = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Подтвердить',
                                                             callback_data=f'finishbooking'),
                                        InlineKeyboardButton(text='Отмена',
                                                             callback_data=f'back_to_menu_callback'),
                                    ]
                                ])
    return kb
