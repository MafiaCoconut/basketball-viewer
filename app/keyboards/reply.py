from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)

rkr = ReplyKeyboardRemove()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Главное меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)