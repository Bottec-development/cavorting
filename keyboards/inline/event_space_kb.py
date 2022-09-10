from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.event_space_config import EVENTS_SPACE, EVENTS_SPACE_HALL_SELECT
from keyboards.callback_datas import event_space_callback


async def select_event_space():
    menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=EVENTS_SPACE[0],
                                                             callback_data=event_space_callback.new(t='eventspace',
                                                                                                    d=0)),
                                        InlineKeyboardButton(text=EVENTS_SPACE[1],
                                                             callback_data=event_space_callback.new(t='eventspace',
                                                                                                    d=1)),
                                    ],
                                    [
                                        InlineKeyboardButton(text=EVENTS_SPACE[2],
                                                             callback_data=event_space_callback.new(t='eventspacehall',
                                                                                                    d=2)),
                                    ],
                                    [
                                        InlineKeyboardButton(text=EVENTS_SPACE[3],
                                                             callback_data=event_space_callback.new(t='eventspace',
                                                                                                    d=3)),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад',
                                                             callback_data=f'back_to_menu_callback'),
                                    ],
                                ])
    return menu


async def desc_event_space_kb():
    menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Забронировать',
                                                             callback_data=f'acceptBooking'),
                                        InlineKeyboardButton(text='Позвонить',
                                                             callback_data=f'calltoadmin'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='К выбору пространств',
                                                             callback_data=f'eventspace'),
                                    ],
                                ])
    return menu


async def select_places_conf_hall():
    btns = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[[InlineKeyboardButton(text=f'{text}',
                                                                       callback_data=event_space_callback.new(
                                                                           t='spacehall', d=f'{data}'))] for data, text
                                                 in EVENTS_SPACE_HALL_SELECT.items()])
    btns.add(
        InlineKeyboardButton(text='Назад',
                             callback_data=f'eventspace'),
    )

    return btns
