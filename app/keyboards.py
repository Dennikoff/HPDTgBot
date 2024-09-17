from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Полезная информация")],
        [KeyboardButton(text="Запись на консультацию")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню...",
)