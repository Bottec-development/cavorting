from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.event_space_config import EVENTS_SPACE


async def select_event_space():
    menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=EVENTS_SPACE[0],
                                                             callback_data=f'eventSpace_1'),
                                        InlineKeyboardButton(text=EVENTS_SPACE[1],
                                                             callback_data=f'eventSpace_2'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=EVENTS_SPACE[2],
                                                             callback_data=f'eventSpace_3'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=EVENTS_SPACE[3],
                                                             callback_data=f'eventSpace_4'),
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


async def select_places_conf_hall(places):
    btns = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[[InlineKeyboardButton(text=f'{x}',
                                                                       callback_data=f'selectPlace_{x}')] for x in places])
    btns.add(
        InlineKeyboardButton(text='Назад',
                             callback_data=f'eventspace'),
    )
    return btns
