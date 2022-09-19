from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.kb_info import back

router = Router()


@router.message(Text(text="О магазине", text_ignore_case=True))
async def start_shopping(message: Message):
    await message.answer("Наш магазин специализируется на . Головной офис - г.Москва, улица Пушкина, дом Колотушкина.", reply_markup=back())
