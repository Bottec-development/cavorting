from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Text

from keyboards.inline.main_inline_kb import menu_keyboard
from keyboards.inline.meeting_rooms_kb import time_piaker

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer(text="Привет👋\nЧто тебя интересует?)",
                         reply_markup=await menu_keyboard())


@dp.callback_query_handler(Text(startswith="back_to_menu_callback"))
async def main_menu_from_callback(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Привет👋\nЧто тебя интересует?)",
                              reply_markup=await menu_keyboard())
