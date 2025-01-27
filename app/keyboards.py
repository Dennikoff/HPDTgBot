from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from app.const import KeyboardConts, MessageHandlerConsts

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

def get_post_keyboard(post_url):
	return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Смотреть пост", url=post_url)]
    ])

def create_posts_menu():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="post_1"),
            InlineKeyboardButton(text="2", callback_data="post_2"),
            InlineKeyboardButton(text="3", callback_data="post_3"),
            InlineKeyboardButton(text="4", callback_data="post_4")
        ]
    ])
    return markup