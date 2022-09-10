from aiogram import types
from aiogram.dispatcher.filters import Text

from data.config import ADMIN_ID
from keyboards.inline.actions_for_manager import actions_manager
from keyboards.inline.parking_kb import parking_keyboard, parking_site, main_parking
from loader import dp


@dp.callback_query_handler(Text(equals='parling'))
async def show_parking_menu(call: types.CallbackQuery):
    keyboard = await parking_keyboard(call.message.chat.id)
    await call.message.edit_text('\n'.join(['Для обнуления парковки тебе понадобятся:\n',
                                            '🔸Номер пропуска (первые 10 цифр)',
                                            '🔸Номер транспортного средства',
                                            '🔸ФИО / наименование компании']), reply_markup=keyboard)


@dp.callback_query_handler(Text(equals='pay_parking'))
async def pay_for_parking(call: types.CallbackQuery):
    await call.message.edit_text('Переход на сайт с формой', reply_markup=parking_site)


@dp.callback_query_handler(Text(startswith='chat_parking_'))
async def chat_with_manager_parking(call: types.CallbackQuery):
    #  Здесь запрос к БД, получаем менеджеров
    await call.message.edit_text('Отправил запрос о начале чата к менеджерам.\n'
                                 'Ожидайте ответа.', reply_markup=main_parking)

    await dp.bot.send_message(
        chat_id=ADMIN_ID,
        text=f'Поступил запрос об обнулении парковки\n'
             f'Выберите действие на клавиатуре.', reply_markup=await actions_manager(call.message.chat.id)
    )
