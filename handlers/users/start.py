from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.main_inline_kb import menu_keyboard
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer(text="Привет👋\nЧто тебя интересует?)",
                         reply_markup=await menu_keyboard())