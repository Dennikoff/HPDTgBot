from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.middleware import check_subscription_middleware
from app.const import MessageHandlerConsts
import app.keyboards as kb

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
'''
Привет! Добро пожаловать!

На связи Харке Виктория Валентивна, КМН, Доцент.
Данный бот отвечает на самые частые вопросы, задаваемые на ортодонтическом приёме, и также содержит полезную информацию для пациентов.
''', reply_markup=kb.main_keyboard)



    
@router.message(F.text.lower() == MessageHandlerConsts.ABOUT_US.lower())
@check_subscription_middleware
async def about_us(message: Message):
    await message.answer(MessageHandlerConsts.ABOUT_US, reply_markup=kb.main_return_keyboard)

@router.message(F.text.lower() == MessageHandlerConsts.INFO.lower())
@check_subscription_middleware
async def about_us(message: Message):
    await message.answer(MessageHandlerConsts.INFO, reply_markup=kb.main_return_keyboard)

@router.message(F.text.lower() == MessageHandlerConsts.CONSULTATION.lower())
@check_subscription_middleware
async def about_us(message: Message):
    await message.answer(MessageHandlerConsts.CONSULTATION, reply_markup=kb.main_return_keyboard)

@router.message(F.text.lower() == MessageHandlerConsts.MAIN_RETURN.lower())
@check_subscription_middleware
async def handle_all_messages(message: Message):
    await message.bot.send_message(message.chat.id, f"Выберите один из пунктов.", reply_markup=kb.main_keyboard)

@router.message()
@check_subscription_middleware
async def handle_all_messages(message: Message):
    await message.bot.send_message(message.chat.id, f"Я вас не понимаю. Выберите один из пунктов.", reply_markup=kb.main_keyboard)