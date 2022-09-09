from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from states.chat import Chat


@dp.callback_query_handler(Text(startswith='cparking_'))
async def chat_parking_manager(call: types.CallbackQuery):
    data = call.data.split('_')[1]
    client_id = call.data.split('_')[2]

    if data == 'yes':
        await call.message.edit_text('Вы перенаправлены в чат.\n'
                                     'Чтобы его остановить, воспользуйтесь командой /stop_dialog')
        await Chat.Manager.set()

        state_manager = dp.current_state(chat=call.message.chat.id, user=call.message.chat.id)

        await state_manager.update_data(
            {
                'client_id': client_id
            }
        )

        await dp.bot.send_message(
            chat_id=int(client_id),
            text='Вы перенаправлены в чат.\n'
                 'Чтобы его остановить, воспользуйтесь командой /stop_dialog'
        )

        state = dp.current_state(chat=client_id, user=client_id)
        await state.set_state(Chat.Client)
        await state.update_data(
            {
                'manager_id': call.message.chat.id
            }
        )

    elif data == 'no':
        await call.message.edit_text('Вы успешно отказались от чата с клиентом.')

        await dp.bot.send_message(
            chat_id=int(client_id),
            text='В начале чата было отказано.'
        )
