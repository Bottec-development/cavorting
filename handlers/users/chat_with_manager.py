from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.parking_kb import go_menu
from loader import dp
from states.chat import Chat


@dp.message_handler(state=Chat.Client)
async def chat_client(message: types.Message, state: FSMContext):
    data = await state.get_data()
    manager_id = data.get('manager_id')
    if message.text == '/stop_dialog':
        await state.reset_state(with_data=True)

        state_manager = dp.current_state(chat=manager_id, user=manager_id)
        await state_manager.reset_state(with_data=True)

        await message.answer('Вы успешно остановили чат.', reply_markup=go_menu)

        await dp.bot.send_message(
            chat_id=manager_id,
            text='Чат был остановлен клиентом.'
        )
    else:
        text = message.text

        await dp.bot.send_message(
            chat_id=manager_id,
            text=text
        )


@dp.message_handler(state=Chat.Manager)
async def chat_manager(message: types.Message, state: FSMContext):
    data = await state.get_data()
    client_id = data.get('client_id')
    if message.text == '/stop_dialog':
        await state.reset_state(with_data=True)

        state_client = dp.current_state(chat=client_id, user=client_id)
        await state_client.reset_state(with_data=True)

        await message.answer('Вы успешно остановили чат.', reply_markup=go_menu)

        await dp.bot.send_message(
            chat_id=client_id,
            text='Чат был остановлен менеджером.'
        )
    else:
        text = message.text

        await dp.bot.send_message(
            chat_id=client_id,
            text=text
        )
