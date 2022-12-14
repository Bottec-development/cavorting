from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_datas import standard_tariff, mini_office_choice, smart_office_choice, booking_callback


async def name_and_description():
    dont_fix_description = "Доступ с 9:00 до 21:00." \
                           "\nПереговорная на 4 персоны* - до 2ч." \
                           "\nПечать ч/б* - 40 л." \
                           "\n\nЧас - 390 ₽" \
                           "\nДень - 1170 ₽" \
                           "\n5 дней - 4990 ₽" \
                           "\n10 дней - 8190 ₽" \
                           "\nМесяц - 12645 ₽" \
                           "\n2 месяца - 23990 ₽" \
                           '\n"Продление"** - 11515 ₽' \
                           '\n\n* - в зависимости от выбранного тарифа.' \
                           '\n** - после приобретения тарифа «2 месяца» / для финалистов ' \
                           'Акселерационной программы «Калибр» / для клиентов, использовавших любую ' \
                           'из основных услуг в коворкинге «Калибр» в период 01.06.2022 – 01.09.2022'
    fix_description = "Доступ 24/7" \
                      "\nПереговорная на 4 персоны - 4 ч." \
                      "\nПечать ч/б - 80 л." \
                      "\n\nЦены указаны за месяц пользования услугой." \
                      '\n"Месяц" - 19900 ₽' \
                      '\n"2 месяца" - 18095 ₽' \
                      '\n"Продление"* - 17910 ₽' \
                      '\n"6 месяцев" - 16415 ₽' \
                      '\n\n* - после приобретения тарифа «2 месяца» / для финалистов Акселерационной ' \
                      'программы «Калибр» / для клиентов, использовавших любую из основных услуг ' \
                      'в коворкинге «Калибр» в период 01.06.2022 – 01.09.2022'
    team_fix_description = "Доступ 24/7" \
                           "\nПереговорная на 4 персоны - 1 ч. (на чел. в месяц)" \
                           "\nПечать ч/б - 20 л. (на чел. в месяц)" \
                           "\n\nЦены указаны за месяц пользования услугой." \
                           '\n"Месяц" - 15800 ₽' \
                           '\n"2 месяца" - 14220 ₽' \
                           '\n"Продление"* - 13430 ₽' \
                           '\n"6 месяцев" - 12320 ₽' \
                           '\n\n* - после приобретения тарифа «2 месяца» / для финалистов Акселерационной ' \
                           'программы «Калибр» / для клиентов, использовавших любую из ' \
                           'основных услуг в коворкинге «Калибр» в период 01.06.2022 – 01.09.2022'
    mini_office = "Доступ 24/7" \
                  "\nКондиционер" \
                  "\nВозможность использования, с письменного разрешения Исполнителя, " \
                  "адреса рабочего места, в качестве адреса места нахождения постоянно " \
                  "действующего исполнительного органа юридического лица"
    smart_office_description = mini_office
    return {
        'Don`t Fix': dont_fix_description,
        'Fix': fix_description,
        'Team Fix': team_fix_description,
        'Мини-офис': mini_office,
        'Smart-офис': smart_office_description
    }


async def mini_office_description():
    person_1 = "Доступ 24/7" \
               "\nПереговорная на 4 персоны - 2 ч." \
               "\nПечать ч/б - 80 л." \
               "\nБиблиотека ('Будни') - 1 ч." \
               "\n\nЦены указаны за месяц пользования услугой." \
               '\n"Месяц" - 19900 ₽' \
               '\n"2 месяца" - 18905 ₽' \
               '\n"Продление"* - 17910 ₽' \
               '\n"6 месяцев" - 16415 ₽' \
               '\n\n* - после приобретения тарифа «2 месяца» / для финалистов Акселерационной ' \
               'программы «Калибр» / для клиентов, использовавших любую из основных услуг в коворкинге ' \
               '«Калибр» в период 01.06.2022 – 01.09.2022'
    person_3 = "Доступ 24/7" \
               "\nКондиционер" \
               "\nПереговорная на 4 персоны - 3 ч." \
               "\nПереговорная на 8 персон - 2 ч." \
               "\nПечать ч/б - 240 л." \
               '\nИнтерактивная зона ("Будни") - 1 ч.' \
               "\n\nЦены указаны за месяц пользования услугой." \
               '\n"Месяц" - 81900 ₽' \
               '\n"2 месяца" - 77805 ₽' \
               '\n"Продление"* - 73710 ₽' \
               '\n"6 месяцев" - 69615 ₽' \
               '\n\n* - после приобретения тарифа «2 месяца» / для финалистов Акселерационной программы «Калибр» / ' \
               'для клиентов, использовавших любую из основных услуг ' \
               'в коворкинге «Калибр» в период 01.06.2022 – 01.09.2022'
    person_4 = "Доступ 24/7" \
               "\nКондиционер" \
               "\nПереговорная на 4 персоны - 3 ч." \
               "\nПереговорная на 8 персон - 3 ч." \
               "\nПечать ч/б - 320 л." \
               '\nИнтерактивная зона + библиотека ("Будни") - 1 ч.' \
               "\n\nЦены указаны за месяц пользования услугой." \
               '\n"Месяц" - 99900 ₽' \
               '\n"2 месяца" - 94905 ₽' \
               '\n"Продление"* - 89910 ₽' \
               '\n"6 месяцев" - 84915 ₽' \
               '\n\n* - после приобретения тарифа «2 месяца» / для финалистов Акселерационной программы «Калибр» / ' \
               'для клиентов, использовавших любую из основных услуг ' \
               'в коворкинге «Калибр» в период 01.06.2022 – 01.09.2022'
    person_8 = "Доступ 24/7" \
               "\nКондиционер" \
               "\nПереговорная на 4 персоны - 4 ч." \
               "\nПереговорная на 8 персон - 3 ч." \
               "\nПечать ч/б - 400 л." \
               '\nИнтерактивная зона + библиотека ("Будни") - 1 ч.' \
               '\nКонференц-зал до 50 мест ("Будни") - 1 ч.' \
               "\n\nЦены указаны за месяц пользования услугой." \
               '\n"Месяц" - 188200 ₽' \
               '\n"2 месяца" - 178790 ₽' \
               '\n"Продление"* - 169380 ₽' \
               '\n"6 месяцев" - 159570 ₽' \
               '\n\n* - после приобретения тарифа «2 месяца» / для финалистов Акселерационной программы «Калибр» / ' \
               'для клиентов, использовавших любую из основных услуг в коворкинге «Калибр» ' \
               'в период 01.06.2022 – 01.09.2022'
    person_20 = "Доступ 24/7" \
                "\nКондиционер" \
                "\nПереговорная на 4 персоны - 5 ч" \
                "\nПереговорная на 8 персон - 4 ч." \
                "\nПечать ч/б - 500 л." \
                '\nИнтерактивная зона + библиотека ("Будни") - 2 ч.' \
                '\nКонференц-зал до 50 мест ("Будни") - 2 ч.' \
                "\n\nЦены указаны за месяц пользования услугой." \
                '\n"Месяц" - 349900 ₽' \
                '\n"2 месяца" - 332405 ₽' \
                '\n"Продление"* - 314910 ₽' \
                '\n"6 месяцев" - 297415 ₽' \
                '\n\n* - после приобретения тарифа «2 месяца» / для финалистов Акселерационной программы «Калибр» / ' \
                'для клиентов, использовавших любую из основных услуг в коворкинге ' \
                '«Калибр» в период 01.06.2022 – 01.09.2022'
    return {
        '1_person': person_1,
        '3_person': person_3,
        '4_person': person_4,
        '8_person': person_8,
        '20_person': person_20,
    }


async def main_tariff_kb():
    button_text = await name_and_description()
    keys = list(button_text.keys())
    kb = InlineKeyboardMarkup(row_width=3)
    button_1 = InlineKeyboardButton(text=keys[0], callback_data=standard_tariff.new(office=keys[0], type="1"))
    button_2 = InlineKeyboardButton(text=keys[1], callback_data=standard_tariff.new(office=keys[1], type="1"))
    button_3 = InlineKeyboardButton(text=keys[2], callback_data=standard_tariff.new(office=keys[2], type="1"))
    button_4 = InlineKeyboardButton(text=keys[3], callback_data=f'mini_office')
    button_5 = InlineKeyboardButton(text=keys[4], callback_data=f'smart_office')
    back_to_menu = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'back_to_menu_callback')
    kb.row(button_1, button_2, button_3)
    kb.row(button_4, button_5)
    kb.row(back_to_menu)
    return kb


async def mini_office_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    choice = {
        'На 1 персону': "1_person",
        'На 3 персоны': "3_person",
        'На 4 персоны': "4_person",
    }
    for i in choice:
        button = InlineKeyboardButton(text=i, callback_data=mini_office_choice.new(person=choice[i], type="2"))
        kb.insert(button)
    back = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'tariff')
    kb.insert(back)
    return kb


async def smart_office_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    choice = {
        'На 8 персон': "8_person",
        'На 20 персон': "20_person",
    }
    keys = list(choice.keys())
    button = InlineKeyboardButton(text=keys[0], callback_data=smart_office_choice.new(person=choice[keys[0]], type="3"))
    button_2 = InlineKeyboardButton(text=keys[1],
                                    callback_data=smart_office_choice.new(person=choice[keys[1]], type="3"))
    kb.row(button, button_2)
    back = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'tariff')
    kb.insert(back)
    return kb


async def standard_tariff_kb(office_type):
    kb = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton(text="Забронировать",
                                    callback_data=booking_callback.new(t="booking", o=office_type))
    button_2 = InlineKeyboardButton(text="Позвонить", callback_data=f'send_phone_tariff')
    button_3 = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'tariff_with_photo')
    kb.row(button_1, button_2)
    kb.insert(button_3)
    return kb


async def back_to_tariff():
    kb = InlineKeyboardMarkup(row_width=1)
    to_information = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'tariff_with_photo')
    kb.insert(to_information)
    return kb
