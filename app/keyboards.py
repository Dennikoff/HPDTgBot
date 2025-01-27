from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from const import KeyboardConts, MessageHandlerConsts

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=MessageHandlerConsts.ABOUT_US)],
        [KeyboardButton(text=MessageHandlerConsts.INFO)],
        [KeyboardButton(text=MessageHandlerConsts.CONSULTATION)],
    ],
    resize_keyboard=True,
    input_field_placeholder=KeyboardConts.CHOOSE_MENU,
)

main_return_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=MessageHandlerConsts.MAIN_RETURN)],
    ],
    resize_keyboard=True,
    input_field_placeholder=KeyboardConts.CHOOSE_MENU,
)