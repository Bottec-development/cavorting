from aiogram.dispatcher.filters.state import State, StatesGroup


class MeetRoomBookingStage_1(StatesGroup):
    select_date = State()
    select_time = State()

class MeetRoomBookingStage_2(StatesGroup):
    fio= State()
    company = State()
    telephone = State()