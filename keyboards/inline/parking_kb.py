from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import SITE_URL


async def parking_keyboard(client_id):
    parking = InlineKeyboardMarkup(row_width=3, inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Обнулить и оплатить', url=SITE_URL)
        ],
        [
            InlineKeyboardButton(text='Обнулить (счет для компании)', callback_data=f'chat_parking_{client_id}')
        ],
        [
            InlineKeyboardButton(text='В меню', callback_data='back_to_menu_callback')
        ]
    ])
    return parking


parking_site = InlineKeyboardMarkup(row_width=3, inline_keyboard=
[
    [
        InlineKeyboardButton(text='Перейти', url=SITE_URL)
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='parling')
    ]
])

main_parking = InlineKeyboardMarkup(row_width=3, inline_keyboard=
                                    [
                                        [
                                            InlineKeyboardButton(text='Назад.', callback_data='parling')
                                        ]
                                    ])

go_menu = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='В меню', callback_data='back_to_menu_callback')
                                   ]
                               ])