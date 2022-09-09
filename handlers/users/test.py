from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.misc.bitrix import create_lid


@dp.message_handler(Command("test"))
async def bot_start(message: types.Message):
    await create_lid("Артем", "Романович", "Козлов", "79779567896", "ООО Телеграм", 1302, 314910.00)
