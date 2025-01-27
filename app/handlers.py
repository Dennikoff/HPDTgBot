from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
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

posts = {
    '1': 'https://telegra.ph/Test-01-27-311',
    '2': 'https://telegra.ph/Test-01-27-311',
    '3': 'https://telegra.ph/Test-01-27-311',
    '4': 'https://telegra.ph/Test-01-27-311'
}



    
@router.message(F.text.lower() == MessageHandlerConsts.ABOUT_US.lower())
@check_subscription_middleware
async def about_us(message: Message):
    await message.answer(MessageHandlerConsts.ABOUT_US, reply_markup=kb.main_return_keyboard)


@router.message(F.text.lower() == MessageHandlerConsts.INFO.lower())
@check_subscription_middleware
async def information(message: Message):
    keyboard = kb.get_post_keyboard('https://telegra.ph/Test-01-27-311')
    await message.answer(MessageHandlerConsts.INFO, reply_markup=keyboard)


@router.message(F.text.lower() == MessageHandlerConsts.CONSULTATION.lower())
@check_subscription_middleware
async def consultation(message: Message):
    await message.answer(MessageHandlerConsts.CONSULTATION, reply_markup=kb.create_posts_menu())


@router.message(F.text.lower() == MessageHandlerConsts.MAIN_RETURN.lower())
@check_subscription_middleware
async def handle_return_message(message: Message):
    await message.bot.send_message(message.chat.id, f"Выберите один из пунктов.", reply_markup=kb.main_keyboard)


@router.message()
@check_subscription_middleware
async def handle_all_messages(message: Message):
    await message.bot.send_message(message.chat.id, f"Я вас не понимаю. Выберите один из пунктов.", reply_markup=kb.main_keyboard)