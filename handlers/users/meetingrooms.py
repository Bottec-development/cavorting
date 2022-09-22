from datetime import datetime
from typing import Dict

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram_calendar import SimpleCalendar, simple_cal_callback

from data.config import ADMIN_TELEPHONE
from keyboards.inline.meeting_rooms_kb import meeting_person, calandar_kb, finish_first_stage_booking, time_piaker, \
    meeting_person_count, meeting_type_room, close_telephone_btn
from loader import dp
from states.meeting_room_booking import MeetRoomBookingStage_1
from utils.misc.time_peaker import inline_timepicker


@dp.callback_query_handler(Text(startswith="calltoadmin"))
async def open_telephone(call: types.CallbackQuery):
    await call.message.answer_contact(phone_number=ADMIN_TELEPHONE,
                                      first_name="Коворкинг Калибр",
                                      reply_markup=await close_telephone_btn())

@dp.callback_query_handler(Text(startswith="closetelephone"))
async def close_telephone(call: types.CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(Text(startswith="meetingrooms"))
async def meet_room_start(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('\n'.join(['Переговорные комнаты\n',
                                         'Переговорный стол, кресла, Wi-Fi, электричество, кондиционер.']),
                              reply_markup=await meeting_person())

@dp.callback_query_handler(Text(startswith="meetingroompeopletype"))
async def meet_room_start(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Выберите тип персон', reply_markup=await meeting_type_room())

@dp.callback_query_handler(Text(startswith="meetingroompeoplecount"))
async def meet_room_start(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Выберите кол-во персон', reply_markup=await meeting_person_count())

@dp.callback_query_handler(Text(startswith="personType"))
async def meet_room_person_type(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'type_person': int(call.data.split("_")[1])})
    await call.message.delete()
    await call.message.answer("Выберите кол-во персон", reply_markup=await meeting_person_count())

@dp.callback_query_handler(Text(startswith="personCount"))
async def meet_room_person_count(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'type_booking': 1, 'personCount': call.data.split("_")[1]})
    await call.message.delete()


    await call.message.answer("Выберите дату бронирования", reply_markup=await calandar_kb())
    await MeetRoomBookingStage_1.select_date.set()


@dp.callback_query_handler(simple_cal_callback.filter(), state=MeetRoomBookingStage_1.select_date)
async def booking_date(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    date_now = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    selected, date = await SimpleCalendar().process_selection(call, callback_data)
    if selected:
        await call.message.delete()
        print(date)
        print(date_now)
        if date < date_now:
            await call.message.answer(text="Выбранная дата не может быть раньше текущей!",
                                      reply_markup=await calandar_kb())
            return
        # проверка на возможность выбора даты
        await state.update_data({"booking_date": date.strftime("%Y-%m-%d")})
        await call.message.answer("Выберите время бронирования", reply_markup=await time_piaker())
        await MeetRoomBookingStage_1.select_time.set()


@dp.callback_query_handler(inline_timepicker.filter(), state=MeetRoomBookingStage_1.select_time)
async def cb_handler(query: types.CallbackQuery, callback_data: Dict[str, str], state: FSMContext):
    await query.answer()
    handle_result = inline_timepicker.handle(query.from_user.id, callback_data)

    if handle_result is not None:
        # проверка на возможность выбора времени
        state_data = await state.get_data()
        await state.update_data({"booking_time": handle_result})
        await query.bot.edit_message_text("\n".join([f"Кол-во персон: {state_data['personCount']}",
                                                     f"Тип персон: {'Резидентны' if state_data['type_person'] == 1 else 'Для всех клиентов'}",
                                                     f"Дата бронирования: {state_data['booking_date']}",
                                                     f"Время бронирования: {handle_result}"]),
                                          chat_id=query.from_user.id,
                                          message_id=query.message.message_id,
                                          reply_markup=await finish_first_stage_booking())
        await state.reset_state(with_data=False)
    else:
        await query.bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                                  message_id=query.message.message_id,
                                                  reply_markup=inline_timepicker.get_keyboard())
