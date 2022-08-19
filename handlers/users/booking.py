import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.event_space_config import EVENTS_SPACE
from keyboards.inline.meeting_rooms_kb import all_finish_booking
from loader import dp
from states.meeting_room_booking import MeetRoomBookingStage_2


@dp.callback_query_handler(Text(startswith="acceptBooking"))
async def acceptBooking(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await MeetRoomBookingStage_2.fio_or_company_name.set()
    await call.message.answer('Введите ваше ФИО или название компании')

@dp.message_handler(state=MeetRoomBookingStage_2.fio_or_company_name)
async def fio_or_company_name(message: types.Message, state: FSMContext):
    await state.update_data({"name": message.text})
    await MeetRoomBookingStage_2.telephone.set()
    await message.answer("Введите ваш контактный номер телефона для связи")


@dp.message_handler(state=MeetRoomBookingStage_2.telephone)
async def booking_telephone(message: types.Message, state: FSMContext):
    clear_phone = re.sub(r'\D', '', message.text)
    result = re.match(r'^[78]?\d{10}$', clear_phone)
    if not result:
        await message.answer(text="Указан неверный номер телефона\nПример 71234567890!")
        return
    else:
        await state.update_data({"telephone": int(message.text)})
        await state.reset_state(with_data=False)
        await finish_booking(message, state)


async def finish_booking(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    if "type_booking" in state_data and state_data['type_booking']:
        text = "\n".join([f"Кол-во персон: {state_data['personCount']}",
                   f"Дата бронирования: {state_data['booking_date']}",
                   f"Время бронирования: {state_data['booking_time']}",
                   f"Забронировал: {state_data['name']}",
                   f"Номер телефона: {state_data['telephone']}"])
    else:
        text = "\n".join([f"Забронировали: {EVENTS_SPACE[int(state_data['space_type'])-1]}",
                   f"Кол-во мест: {state_data['space_place']}" if "space_place" in state_data else "",
                   f"Забронировал: {state_data['name']}",
                   f"Номер телефона: {state_data['telephone']}"])
    await state.finish()
    #отправка данных на битрекс
    await message.answer(f"Бронь успешно создана\n{text}", reply_markup=await all_finish_booking())

