from aiogram.types import InputFile
EVENTS_SPACE = [
    'Интерактивная зона',
    'Библиотека',
    'Конференц-зал',
    'Интерактивная зона+Библиотека',
]

EVENTS_SPACE_HALL_SELECT = {
    'hall_50': 'До 50 мест',
    'hall_80': 'До 80 мест',
    'hall_130': 'До 130 мест',
    'all_hall': 'Весь этаж',
}


async def get_text_photo_eventspace(type_space):
    interact_zone = ' Цена указана за час пользования.*\n' \
                    '\n"Будни" (пн-чт) / "Выходные" (пт-вс)' \
                    '\n1-3 часа - 5520 | 6900 ₽ / 6900 | 8280 ₽' \
                    '\n4-7 часов - 4410 | 5520 ₽ / 5520 | 6620 ₽' \
                    '\n8 и более часов - 3860 | 4830 ₽ / 4830 | 5800 ₽\n' \
                    '\n* - "День" (10:00-20:00) / "Ночь" (20:01-09:59)'

    library = 'Цена указана за час пользования.*\n' \
              '\n"Будни" (пн-чт) / "Выходные" (пт-вс)' \
              '\n1-3 часа - 3920 | 4900 ₽ / 4900 | 5880 ₽' \
              '\n4-7 часов - 3136 | 3920 ₽ / 3920 | 4704 ₽' \
              '\n8 и более часов - 2744 | 3430 ₽ / 3430 | 4116 ₽\n' \
              '\n* - "День" (10:00-20:00) / "Ночь" (20:01-09:59)'

    interact_library = 'Цена указана за час пользования.*\n' \
                       '\n"Будни" (пн-чт) / "Выходные" (пт-вс)' \
                       '\n1-3 часа - 7920 | 9900 ₽ / 9900 | 11880 ₽' \
                       '\n4-7 часов - 6360 | 7920 ₽ / 7920 | 9500 ₽' \
                       '\n8 и более часов - 5540 | 6930 ₽ / 6930 | 8320 ₽\n' \
                       '\n* - "День" (10:00-20:00) / "Ночь" (20:01-09:59)'

    conf_hall = 'Конференц-зал\n' \
                '\nИнформационная поддержка мероприятия, публикация анонса мероприятия на ресурсах коворкинга, административная поддержка мероприятия.\n' \
                '\nДля клиентов, использующих одну из основных услуг коворкинга "Калибр" или арендующих территории Технопарка "Калибр" аренда пространства для мероприятий осуществляется со скидкой.'

    hall_50 = 'Цена указана за час пользования.*\n' \
              '\n"Будни" (пн-чт) / "Выходные" (пт-вс)' \
              '\n1-3 часа - 5520 | 6900 ₽ / 6900 | 8280 ₽' \
              '\n4-7 часов - 4410 | 5520 ₽ / 5520 | 6620 ₽' \
              '\n8 и более часов - 3860 | 4830 ₽ / 4830 | 5800 ₽\n' \
              '\n* - "День" (10:00-20:00) / "Ночь" (20:01-09:59)'

    hall_80 = 'Цена указана за час пользования.*\n' \
              '\n"Будни" (пн-чт) / "Выходные" (пт-вс)' \
              '\n1-3 часа - 7920 | 9900 ₽ / 9900 | 11880 ₽' \
              '\n4-7 часов - 6360 | 7920 ₽ / 7920 | 9500 ₽' \
              '\n8 и более часов - 5540 | 6930 ₽ / 6930 | 8320 ₽\n' \
              '\n* - "День" (10:00-20:00) / "Ночь" (20:01-09:59)'

    hall_130 = 'Цена указана за час пользования.*\n' \
               '\n"Будни" (пн-чт) / "Выходные" (пт-вс)' \
               '\n1-3 часа - 11120 | 13900 ₽ / 13900 | 16680 ₽' \
               '\n4-7 часов - 8890 | 11120 ₽ / 11120 | 13350 ₽' \
               '\n8 и более часов - 7790 | 9730 ₽ / 9730 | 11680 ₽\n' \
               '\n* - "День" (10:00-20:00) / "Ночь" (20:01-09:59)'

    all_hall = 'Цена указана за час пользования.*\n' \
               '\n"Будни" (пн-чт) / "Выходные" (пт-вс)' \
               '\n1-3 часа - 15120 | 18900 ₽ / 18900 | 16680 ₽' \
               '\n4-7 часов - 12090 | 15120 ₽ / 15120 | 13344 ₽' \
               '\n8 и более часов - 10584 | 13230 ₽ / 13230 | 11680 ₽\n' \
               '\n* - "День" (10:00-20:00) / "Ночь" (20:01-09:59)'

    if type_space == EVENTS_SPACE[0]:
        return interact_zone, InputFile('img/interact_zone.jpg')
    elif type_space == EVENTS_SPACE[1]:
        return library, InputFile('img/library.jpg')
    elif type_space == EVENTS_SPACE[2]:
        return conf_hall
    elif type_space == EVENTS_SPACE[3]:
        return interact_library, InputFile('img/interact_zone_library.jpg')
    elif type_space == "hall_50":
        return hall_50, InputFile('img/conf_50.jpg')
    elif type_space == "hall_80":
        return hall_80, InputFile('img/conf_80.jpg')
    elif type_space == "hall_130":
        return hall_130, InputFile('img/conf_130.jpg')
    elif type_space == "all_hall":
        return all_hall, InputFile('img/conf_all.jpg')
