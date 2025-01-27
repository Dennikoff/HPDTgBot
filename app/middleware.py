from config import channel_id, channel_url
from functools import wraps
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

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