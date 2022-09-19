import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import h_start, h_shopping, h_info, h_support 

load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(h_start.router)
    dp.include_router(h_shopping.router)
    dp.include_router(h_info.router)
    dp.include_router(h_support.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
