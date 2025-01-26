from aiogram import Bot, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import channel_id, channel_url


import app.keyboards as kb

router = Router()

async def check_subscription(message: Message):
    # Получаем информацию о пользователе в чате
    chat_member = await message.bot.get_chat_member(channel_id, message.from_user.id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        # Пользователь подписан
        return True
    else:
        # Пользователь не подписан
        return False

async def ask_for_subscription(message: Message):
    # Создаем inline клавиатуру с кнопкой для перехода на канал
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на канал", url=channel_url)]
    ])
    
    await message.reply("Чтобы использовать этого бота, подпишись на канал:", reply_markup=keyboard)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
'''
Привет! Добро пожаловать!

На связи Харке Виктория Валентивна, КМН, Доцент.
Данный бот отвечает на самые частые вопросы, задаваемые на ортодонтическом приёме, и также содержит полезную информацию для пациентов.
''', reply_markup=kb.main)
    
@router.message()
async def handle_all_messages(message: Message):
    if await check_subscription(message):
        await message.bot.send_message(message.chat.id, f"Я вас не понимаю. Выберите один из пунктов.", reply_markup=kb.main)
    else:
        # Если не подписан, отправляем ссылку на канал
        await ask_for_subscription(message)
    