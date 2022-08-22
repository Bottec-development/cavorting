from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.actions_for_manager import actions_manager
from loader import dp
from states.chat import Chat


@dp.callback_query_handler(Text(equals='askquestion'))
async def support_show(call: types.CallbackQuery):
    msg = await call.message.edit_text('Отправьте свой вопрос и администратор ответит на него в чате.')
    await Chat.GetMessage.set()
    state = dp.current_state(chat=call.message.chat.id, user=call.message.chat.id)
    await state.update_data(
        {
            'message_id': msg.message_id
        }
    )


@dp.message_handler(state=Chat.GetMessage)
async def support_get_message(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    message_id = data.get('message_id')
    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message_id)

    await message.answer('Мы получили ваше сообщение, в скором времени вам ответят.')
    await state.reset_state(with_data=True)
    # тут мы сохраняем в бд вопрос и ид юзера
    # тут мы получаем ид админа и отправляем ему сообщение
    admin_id = 5023654394

    keyboard = await actions_manager(client_id=message.chat.id)
    await dp.bot.send_message(
        chat_id=admin_id,
        text='Поступил новый вопрос.\n'
             f'{text}\n\n'
             f'Выберите действие на клавиатуре', reply_markup=keyboard
    )
