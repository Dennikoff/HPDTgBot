from aiogram import Bot, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import channel_id


import app.keyboards as kb

router = Router()


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
    chat_member = await message.bot.get_chat_member(channel_id, message.from_user.id)
    if chat_member.status in ['member', 'administrator', 'creator']:
        # Пользователь подписан
        await message.bot.send_message(message.chat.id, "Ты подписан на канал, можешь использовать бота!")
    else:
        # Пользователь не подписан
        await message.reply(f"Чтобы использовать этого бота, нужно подписаться на канал! {channel_id}")
    # await message.bot.send_message(message.chat.id, f"Я вас не понимаю. Выберите один из пунктов.", reply_markup=kb.main)
    