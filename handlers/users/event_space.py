from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.event_space_kb import select_event_space, desc_event_space_kb, select_places_conf_hall
from loader import dp


@dp.callback_query_handler(Text(startswith="eventspace"))
async def eventspace(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('\n'.join(['Пространство для мероприятий\n',
                                         'Мультимедийное оборудование, Wi-Fi, электричество, кондиционер, мебель, подготовка помещения в соответствии с ТЗ']),
                              reply_markup=await select_event_space())


@dp.callback_query_handler(Text(startswith="eventSpace_"), lambda c: "3" not in str(c.data))
async def eventspace_without_conf_hall(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data({'space_type': call.data.split("_")[1]})
    await call.message.answer("Тут я получаю какие-то данные для вывода информации",
                              reply_markup=await desc_event_space_kb())


@dp.callback_query_handler(Text(startswith="eventSpace_"), lambda c: "3" in str(c.data))
async def eventspace_conf_hall(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data({'space_type': call.data.split("_")[1]})
    places = [3, 5, 8, 10]
    await call.message.answer("Тут я получаю места в разных конференц залах",
                              reply_markup=await select_places_conf_hall(places))


@dp.callback_query_handler(Text(startswith="selectPlace"), lambda c: "3" not in str(c.data))
async def selectPlace_conf_hall(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data({'space_place': call.data.split("_")[1]})
    place = call.data.split("_")[1]
    await call.message.answer(f"Тут я получаю данные о конф зале на {place} мест",
                              reply_markup=await desc_event_space_kb())
