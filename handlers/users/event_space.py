from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.event_space_config import EVENTS_SPACE, EVENTS_SPACE_HALL_SELECT, get_text_photo_eventspace
from keyboards.callback_datas import event_space_callback
from keyboards.inline.event_space_kb import select_event_space, desc_event_space_kb, select_places_conf_hall
from loader import dp


@dp.callback_query_handler(Text(startswith="eventspace"))
async def eventspace(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('\n'.join(['Пространство для мероприятий\n',
                                         'Мультимедийное оборудование, Wi-Fi, электричество, кондиционер, мебель, подготовка помещения в соответствии с ТЗ']),
                              reply_markup=await select_event_space())


@dp.callback_query_handler(event_space_callback.filter(t="eventspace"))
async def eventspace_without_conf_hall(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    await state.update_data({'space_type': EVENTS_SPACE[int(callback_data.get("d"))]})
    text, photo = await get_text_photo_eventspace(EVENTS_SPACE[int(callback_data.get("d"))])
    await call.message.answer_photo(caption=text, photo=photo,
                                    reply_markup=await desc_event_space_kb())


@dp.callback_query_handler(event_space_callback.filter(t="spacehall"))
async def eventspace_without_conf_hall(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    await state.update_data({'space_type': EVENTS_SPACE_HALL_SELECT[callback_data.get('d')]})
    text, photo = await get_text_photo_eventspace(callback_data.get('d'))
    await call.message.answer_photo(caption=text, photo=photo,
                                    reply_markup=await desc_event_space_kb())


@dp.callback_query_handler(event_space_callback.filter(t="eventspacehall"))
async def eventspace_conf_hall(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text=await get_text_photo_eventspace(EVENTS_SPACE[int(callback_data.get("d"))]),
                              reply_markup=await select_places_conf_hall())
