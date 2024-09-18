from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

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
    