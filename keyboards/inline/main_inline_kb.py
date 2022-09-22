from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def menu_keyboard():
    menu = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Тарифы',
                                                               callback_data=f'tariff'),
                                          InlineKeyboardButton(text='Парковка',
                                                               callback_data=f'parling'),
                                      ],

                                      [
                                          InlineKeyboardButton(text='Переговорные комнаты',
                                                               callback_data=f'meetingrooms'),
                                      ],
                                      # [
                                      #     InlineKeyboardButton(text='Пространство для мероприятий',
                                      #                          callback_data=f'eventspace'),
                                      # ],
                                      [
                                          InlineKeyboardButton(text='Задать вопрос',
                                                               callback_data=f'askquestion'),
                                          InlineKeyboardButton(text='Как добраться',
                                                               callback_data=f'information'),
                                      ],
                                  ])
    return menu
