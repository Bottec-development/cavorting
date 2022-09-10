from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text

from keyboards.inline.main_inline_kb import menu_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer(text="Привет👋\nЧто тебя интересует?)",
                         reply_markup=await menu_keyboard())


@dp.callback_query_handler(Text(startswith="back_to_menu_callback"))
async def main_menu_from_callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    await call.message.answer(text="Привет👋\nЧто тебя интересует?)",
                              reply_markup=await menu_keyboard())
