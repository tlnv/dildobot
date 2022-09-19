from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.kb_support import back


router = Router()


@router.message(Text(text="Техподдержка", text_ignore_case=True))
async def start_shopping(message: Message):
    await message.answer("Часто задаваемые вопросы: 1. Оплата производится только безналичным расчетом? - Да 2.3.", reply_markup=back())
