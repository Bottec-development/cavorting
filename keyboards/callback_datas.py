from aiogram.utils.callback_data import CallbackData

standard_tariff = CallbackData("set", "office", "type")
mini_office_choice = CallbackData("set", "person", "type")
smart_office_choice = CallbackData("set", "person", "type")
booking_callback = CallbackData("set", "o", "t")
event_space_callback = CallbackData("set", "d", "t")