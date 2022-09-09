from aiogram import types
from aiogram.types import InputFile
from aiogram.utils.markdown import hbold

from keyboards.callback_datas import standard_tariff, mini_office_choice, booking_callback
from keyboards.inline.tariff_kb import main_tariff_kb, name_and_description, standard_tariff_kb, mini_office_kb, \
    mini_office_description, smart_office_kb, back_to_tariff
from loader import dp


async def get_tariff_description():
    return 'При бронировании любого тарифа из перечня "Коворкинг", "Мини-офис", ' \
           '"Smart-офис" предоставляются:\n' \
           '- 2 кухонные зоны;Зоны общего пользования\n' \
           '- Интернет до 60 Мб/с;МФУ с индивидуальным доступом\n' \
           '- Бесплатный доступ к мероприятиям ПАО "Калибр"\n' \
           '- Доступ к мероприятиям партнёров ПАО "Калибр" на специальных условиях\n' \
           '- Кофе и снеки в кофейне со скидкой 10% и накопительной системой кэшбека\n' \
           '- Полноценная столовая\n' \
           'Бесплатный доступ к спортивной площадке с условием обязательного допуска к участию любого желающего. П' \
           'ри условии индивидуального пользования спортивной площадкой, данная услуга ' \
           'предоставляется на платной основе по утвержденному тарифу.'


@dp.callback_query_handler(text='tariff')
async def information(call: types.CallbackQuery):
    text = await get_tariff_description()
    await call.message.edit_text(text=text, reply_markup=await main_tariff_kb())


@dp.callback_query_handler(text='tariff_with_photo')
async def information(call: types.CallbackQuery):
    await call.message.delete()
    text = await get_tariff_description()
    await call.message.answer(text=text, reply_markup=await main_tariff_kb())


@dp.callback_query_handler(text='mini_office')
async def show_mini_office(call: types.CallbackQuery):
    office_name = "Мини-офис"
    office_description = await name_and_description()
    string = [f"{hbold(office_name)}\n", office_description[office_name]]
    await call.message.edit_text(text="\n".join(string), reply_markup=await mini_office_kb())


@dp.callback_query_handler(text='smart_office')
async def show_smart_office(call: types.CallbackQuery):
    office_name = "Smart-офис"
    office_description = await name_and_description()
    string = [f"{hbold(office_name)}\n", office_description[office_name]]
    await call.message.edit_text(text="\n".join(string), reply_markup=await smart_office_kb())


@dp.callback_query_handler(standard_tariff.filter(type="1"))
async def information(call: types.CallbackQuery, callback_data: dict):
    await call.message.delete()
    office = callback_data.get("office")
    office_description = await name_and_description()
    string = [f"{hbold(office)}\n", office_description[office]]
    if office == "Don`t Fix":
        photo = InputFile('img/dont_fix.jpg')
    elif office == "Fix":
        photo = InputFile('img/fix.jpg')
    else:
        photo = InputFile('img/team_fix.jpg')
    await call.message.answer_photo(caption="\n".join(string), reply_markup=await standard_tariff_kb(office), photo=photo)


@dp.callback_query_handler(mini_office_choice.filter(type="2"))
async def information(call: types.CallbackQuery, callback_data: dict):
    await call.message.delete()
    person = callback_data.get("person")
    office_description = await mini_office_description()
    if person == "1_person":
        office_name = f"Мини-офис на 1 персону"
        photo = InputFile('img/person_3.jpg')
    elif person == "2_person":
        office_name = f"Мини-офис на 2 персоны"
        photo = InputFile('img/person_3.jpg')
    else:
        office_name = f"Мини-офис на 4 персоны"
        photo = InputFile('img/person_4.jpg')
    string = [f"{hbold(office_name)}\n", office_description[person]]
    await call.message.answer_photo(caption="\n".join(string), reply_markup=await standard_tariff_kb(office_name), photo=photo)


@dp.callback_query_handler(mini_office_choice.filter(type="3"))
async def information(call: types.CallbackQuery, callback_data: dict):
    await call.message.delete()
    person = callback_data.get("person")
    office_description = await mini_office_description()
    if person == "8_person":
        office_name = f"Smart-офис на 8 персон"
        photo = InputFile('img/person_8.jpg')
    else:
        office_name = f"Smart-офис на 20 персон"
        photo = InputFile('img/person_20.jpg')
    string = [f"{hbold(office_name)}\n", office_description[person]]
    await call.message.answer_photo(caption="\n".join(string), reply_markup=await standard_tariff_kb(office_name), photo=photo)


@dp.callback_query_handler(text='send_phone_tariff')
async def send_phone(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_contact(phone_number="89295000656", first_name="Коворкинг", last_name="Калибр",
                                      reply_markup=await back_to_tariff())