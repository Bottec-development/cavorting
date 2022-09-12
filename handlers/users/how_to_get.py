from aiogram import types

from data.config import ADMIN_TELEPHONE
from keyboards.inline.how_to_get_kb import inforamtion_keyboard, back_to_information
from loader import dp


@dp.callback_query_handler(text='information')
async def information(call: types.CallbackQuery):
    await call.message.delete()
    latitude = 55.808735
    longitude = 37.629228
    await call.message.answer_location(latitude=latitude, longitude=longitude,
                                       reply_markup=await inforamtion_keyboard(latitude, longitude))


@dp.callback_query_handler(text='send_phone')
async def send_phone(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_contact(phone_number=ADMIN_TELEPHONE, first_name="Коворкинг", last_name="Калибр",
                                      reply_markup=await back_to_information())


@dp.callback_query_handler(text='send_address')
async def send_phone(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Мы находимся по адресу: улица Годовикова, 9с17",
                              reply_markup=await back_to_information())
