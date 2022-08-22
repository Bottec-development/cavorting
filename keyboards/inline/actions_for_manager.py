from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def actions_manager(client_id):
    actions = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='Начать чат',
                                                                callback_data=f'cparking_yes_{client_id}'),
                                           InlineKeyboardButton(text='Отметить чат',
                                                                callback_data=f'cparking_no_{client_id}')
                                       ],
                                   ])
    return actions
