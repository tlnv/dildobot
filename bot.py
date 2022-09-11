import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)

dispatcher = Dispatcher()


@dispatcher.message(commands=["start"])
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Выбрать товар")],
        [types.KeyboardButton(text="Я еблан")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Привет!")
    await message.answer("Че делать будем?", reply_markup=keyboard)


async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
