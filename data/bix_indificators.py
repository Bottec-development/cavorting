from data.event_space_config import EVENTS_SPACE


async def get_info(office_type):
    DontFix = {
        "час": [390, 1429],
        "День": [1170, 1426],
        "5 дней": [4990, 1426],
        "10 дней": [8190, 1426],
        "Месяц": [12645, 1412],
        "2 месяца": [23990, 1412],
        "«Продление»": [11515, 1428]
    }

    Fix = {
        "Месяц": [19900, 1232],
        "2 месяца": [18905 * 2, 1230],
        "«Продление»": [17910, 1326],
        "6 месяцев": [16415 * 6, 1229],
    }

    FixTeam = {
        "Месяц": [15800, 1379],
        "2 месяца": [14220 * 2, 1227],
        "«Продление»": [13430, 1325],
        "6 месяцев": [12320 * 6, 1228],
    }

    MiniOffice_1 = {
        "Месяц": [19900, 1433],
        "2 месяца": [18905 * 2, 1431],
        "«Продление»": [17910, 1431],
        "6 месяцев": [16415 * 6, 1432],
    }

    MiniOffice_3 = {
        "Месяц": [81900, 1312],
        "2 месяца": [77805 * 2, 1435],
        "«Продление»": [73710, 1413],
        "6 месяцев": [69615 * 6, 1434],
    }

    MiniOffice_4 = {
        "Месяц": [99900, 1308],
        "2 месяца": [94905 * 2, 1436],
        "«Продление»": [89910, 1420],
        "6 месяцев": [84915 * 6, 1437],
    }

    SmartOffice_8 = {
        "Месяц": [188200, 792],
        "2 месяца": [178790 * 2, 1439],
        "«Продление»": [169380, 1414],
        "6 месяцев": [159570 * 6, 1438],
    }

    SmartOffice_20 = {
        "Месяц": [349900, 1302],
        "2 месяца": [332405 * 2, 1430],
        "«Продление»": [314910, 1430],
        "6 месяцев": [297415 * 6, 1440],
    }

    MeetRoom_4_2 = {
        "час": [1100, 1233],
        "5 часов": [990 * 5, 1233],
        "10 часов": [880 * 10, 1233],
        "20 часов": [770 * 20, 1233],
    }

    MeetRoom_8_2 = {
        "час": [2200, 1266],
        "5 часов": [1980 * 5, 1444],
        "10 часов": [1760 * 10, 1445],
        "20 часов": [1540 * 20, 1446],
    }

    MeetRoom_4_1 = {
        "час": [990, 1251],
        "5 часов": [880 * 5, 1251],
        "10 часов": [770 * 10, 1251],
        "20 часов": [690 * 20, 1251],
    }

    MeetRoom_8_1 = {
        "час": [1980, 1249],
        "5 часов": [1760 * 5, 1442],
        "10 часов": [1540 * 10, 1441],
        "20 часов": [1385 * 20, 1443],
    }

    interact_zone = {
        "1-3 час": [5520, 0],
        "4-7 часов": [4410, 0],
        "8 и более часов": [3860, 0],
    }

    library = {
        "1-3 час": [3920, 0],
        "4-7 часов": [3136, 0],
        "8 и более часов": [2744, 0],
        "на всегда": [2744, 0],
    }
    interact_library_zone = {
        "1-3 час": [7920, 0],
        "4-7 часов": [6360, 0],
        "8 и более часов": [5540, 0],
    }

    hall_50 = {
        "1-3 час": [5520, 0],
        "4-7 часов": [4410, 0],
        "8 и более часов": [3860, 0],
    }
    hall_80 = {
        "1-3 час": [7920, 0],
        "4-7 часов": [6360, 0],
        "8 и более часов": [5540, 0],
    }
    hall_130 = {
        "1-3 час": [11120, 0],
        "4-7 часов": [8890, 0],
        "8 и более часов": [7790, 0],
    }
    hall_all = {
        "1-3 час": [15120, 0],
        "4-7 часов": [12090, 0],
        "8 и более часов": [10584, 0],
    }

    if office_type == "Smart-офис на 20 персон":
        return SmartOffice_20
    elif office_type == "Smart-офис на 8 персон":
        return SmartOffice_8
    elif office_type == "Мини-офис на 4 персоны":
        return MiniOffice_4
    elif office_type == "Мини-офис на 3 персоны":
        return MiniOffice_3
    elif office_type == "Мини-офис на 1 персону":
        return MiniOffice_1
    elif office_type == EVENTS_SPACE[0]:
        return interact_zone
    elif office_type == EVENTS_SPACE[1]:
        return library
    elif office_type == EVENTS_SPACE[3]:
        return interact_library_zone
    elif office_type == "До 50 мест":
        return hall_50
    elif office_type == "До 80 мест":
        return hall_80
    elif office_type == "До 130 мест":
        return hall_130
    elif office_type == "Весь этаж":
        return hall_all
    elif office_type == "Don`t Fix":
        return DontFix
    elif office_type == "Fix":
        return Fix
    elif office_type == "Team Fix":
        return FixTeam
    elif office_type == "meet_2_4":
        return MeetRoom_4_2
    elif office_type == "meet_2_8":
        return MeetRoom_8_2
    elif office_type == "meet_1_4":
        return MeetRoom_4_1
    elif office_type == "meet_1_8":
        return MeetRoom_8_1
