import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.bix_indificators import get_info
from keyboards.callback_datas import booking_callback
from keyboards.inline.bitrix_date_keyboard import get_date_kb
from keyboards.inline.booking_kb import accept_booking_kb
from keyboards.inline.meeting_rooms_kb import all_finish_booking
from loader import dp
from states.meeting_room_booking import MeetRoomBookingStage_2
from utils.misc.bitrix import create_lid


@dp.callback_query_handler(Text(startswith="acceptBooking"))
@dp.callback_query_handler(booking_callback.filter(t="booking"))
async def acceptBooking(call: types.CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    if ":" in call.data:
        await state.update_data({'booking_type': call.data.split(":")[1]})
    elif "space_type" not in state_data:
        await state.update_data({'booking_type': f"meet_{state_data['type_person']}_{state_data['personCount']}"})
    elif "space_type" in state_data:
        if "До" in state_data['space_type'] or "Весь этаж" in state_data['space_type']:
            await state.update_data({'space_type': f"Конф. зал {state_data['space_type']}"})

        await state.update_data({'booking_type': state_data['space_type']})
    await call.message.delete()
    await MeetRoomBookingStage_2.fio.set()
    await call.message.answer('Введите ваше ФИО. Пример: Иванов Иван Иванович')


@dp.message_handler(state=MeetRoomBookingStage_2.fio)
async def fio_or_company_name(message: types.Message, state: FSMContext):
    if len(message.text.split(" ")) != 3:
        await message.answer("Ошибка! попробуйте набрать ФИО как в примере! Примере: Иванов Иван Иванович")
        return

    await state.update_data({"name": message.text})
    await MeetRoomBookingStage_2.company.set()
    await message.answer("Введите название вашей компании")


@dp.message_handler(state=MeetRoomBookingStage_2.company)
async def fio_or_company_name(message: types.Message, state: FSMContext):
    await state.update_data({"company": message.text})
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
        await prefinish_booking(message, state)


async def prefinish_booking(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    await message.answer("На сколько вы хотите оформить бронирование?",
                         reply_markup=await get_date_kb(state_data['booking_type']))


@dp.callback_query_handler(booking_callback.filter(t="bxdate"))
async def date_selected(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    key = callback_data.get("o")
    await state.update_data({'key_booking': key})
    await call.message.answer(
        text=f"Ваша заявка: \n{await get_text_prefinish_bookig(state)}\n\nЗавершить бронирование?",
        reply_markup=await accept_booking_kb())


@dp.callback_query_handler(Text(startswith="finishbooking"))
async def date_selected(call: types.CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    #await call.message.delete()
    await call.message.answer(text=f"Заявка оформлена!\nВаша заявка:\n{await get_text_prefinish_bookig(state)}")
    await call.message.answer(f"\nВ скором времени с вами свяжется наш оператор для уточнения остальных деталей.",
                              reply_markup=await all_finish_booking())
    print(state_data)
    if "booking_type" in state_data and "meet" in state_data['booking_type']:
        data = state_data['booking_type'].split("_")
        fin_str = f"Переговорная комната для {'Резидентов' if int(data[1])==1 else 'Группы' if int(data[1])==2 else ''} на {data[2]} места"
    elif "space_type" in state_data or "booking_type" in state_data:
        fin_str = f"{state_data['space_type']}" if "space_type" in state_data else f"Тариф: {state_data['booking_type']}"

    title = f"{fin_str} ({state_data['key_booking']}) {'на ('+str(state_data['booking_date']) +' '+ str(state_data['booking_time'])+')' if 'booking_date' in state_data else ''}"
    names = state_data['name'].split(" ")
    bit_indificator = (await get_info(state_data['booking_type']))[state_data['key_booking']]
    print(title,names[1], names[2], names[0], state_data['telephone'], state_data['company'], bit_indificator[1], float(f"{bit_indificator[0]}.00"))
    await create_lid(title,names[1], names[2], names[0], state_data['telephone'], state_data['company'], bit_indificator[1], float(f"{bit_indificator[0]}.00"))



async def get_text_prefinish_bookig(state: FSMContext):
    state_data = await state.get_data()
    if "type_booking" in state_data and state_data['type_booking']:
        text = "\n".join([
            f"Тип персон: {'Резидентны' if state_data['type_person'] else 'Обычные' if state_data['type_person'] == 2 else ''}",
            f"Кол-во персон: {state_data['personCount']}",
            f"Дата бронирования: {state_data['booking_date']}",
            f"Время бронирования: {state_data['booking_time']}",
            f"Забронировал: {state_data['name']}",
            f"Название компании: {state_data['company']}",
            f"Номер телефона: {state_data['telephone']}",
            f"Стоимость: {(await get_info(state_data['booking_type']))[state_data['key_booking']][0]}",
        ])
    elif "space_type" in state_data or "booking_type" in state_data:
        text = "\n".join([
            f"Забронировали: {state_data['space_type']}" if "space_type" in state_data else f"Тариф: {state_data['booking_type']}",
            f"Время бронирования: {state_data['key_booking']}",
            f"Забронировал: {state_data['name']}",
            f"Название компании: {state_data['company']}",
            f"Номер телефона: {state_data['telephone']}",
            f"Стоимость: {(await get_info(state_data['booking_type']))[state_data['key_booking']][0] if 'space_type' in state_data else (await get_info(state_data['booking_type']))[state_data['key_booking']][0]}"])

    return text
