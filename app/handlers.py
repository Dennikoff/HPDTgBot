from aiogram import Bot, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import channel_id, channel_url
from functools import wraps

import app.keyboards as kb

router = Router()

def check_subscription_middleware(func):
    @wraps(func)
    async def wrapper(message: Message, *args, **kwargs):
        chat_member = await message.bot.get_chat_member(channel_id, message.from_user.id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            return await func(message, *args, **kwargs)
        else:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Перейти на канал", url=channel_url)]
            ])
            return await message.answer("Чтобы использовать этого бота, подпишись на канал:", reply_markup=keyboard)
    return wrapper

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
'''
Привет! Добро пожаловать!

На связи Харке Виктория Валентивна, КМН, Доцент.
Данный бот отвечает на самые частые вопросы, задаваемые на ортодонтическом приёме, и также содержит полезную информацию для пациентов.
''', reply_markup=kb.main)


@router.message()
@check_subscription_middleware
async def handle_all_messages(message: Message):
    await message.bot.send_message(message.chat.id, f"Я вас не понимаю. Выберите один из пунктов.", reply_markup=kb.main)
    