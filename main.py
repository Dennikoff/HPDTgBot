import os
from config import token
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router



async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot has started")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')