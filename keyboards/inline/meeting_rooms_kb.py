import datetime

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_calendar import SimpleCalendar

from utils.misc.time_peaker import inline_timepicker


async def meeting_type_room():
    menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Резидентны',
                                                             callback_data=f'personType_1'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Обычные',
                                                             callback_data=f'personType_2'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад',
                                                             callback_data=f'meetingrooms'),
                                    ],
                                ])
    return menu


async def meeting_person():
    menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Забронировать',
                                                             callback_data=f'meetingroompeopletype'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Позвонить',
                                                             callback_data=f'calltoadmin'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад',
                                                             callback_data=f'back_to_menu_callback'),
                                    ],
                                ])
    return menu


async def meeting_person_count():
    menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='4 персоны',
                                                             callback_data=f'personCount_4'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='8 персон',
                                                             callback_data=f'personCount_8'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад',
                                                             callback_data=f'meetingroompeopletype'),
                                    ],
                                ])
    return menu


async def calandar_kb():
    kb = await SimpleCalendar().start_calendar()
    return kb


async def time_piaker():
    inline_timepicker.init(
        datetime.time(12),
        datetime.time(1),
        datetime.time(23),
        minute_step=5
    )
    return inline_timepicker.get_keyboard()


async def finish_first_stage_booking():
    btns = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Забронировать',
                                                             callback_data=f'acceptBooking'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Отмена',
                                                             callback_data=f'back_to_menu_callback'),
                                    ],
                                ])
    return btns


async def all_finish_booking():
    btns = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Назад',
                                                             callback_data=f'back_to_menu_callback'),
                                    ],
                                ])
    return btns


async def close_telephone_btn():
    btns = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Назад',
                                                             callback_data=f'closetelephone'),
                                    ],
                                ])
    return btns
