from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.kb_start import kb_start


router = Router()


@router.message(commands=["start"])
async def cmd_start(message: Message):
    await message.answer("Здравствуйте! Вы в магазине МАГАЗИН. Тыры пыры описание.", reply_markup=kb_start())


@router.message(Text(text="Вернуться в главное меню", text_ignore_case=True))
async def cmd_start(message: Message):
    await message.answer("Здравствуйте! Вы в магазине МАГАЗИН. Тыры пыры описание.", reply_markup=kb_start())

