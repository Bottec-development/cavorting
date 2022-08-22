from aiogram.dispatcher.filters.state import StatesGroup, State


class Chat(StatesGroup):
    Manager = State()
    Client = State()
    GetMessage = State()
