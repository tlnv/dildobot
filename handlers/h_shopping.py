from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.kb_shopping import kb_choose_category, kb_choose_product, kb_back_to_menu, kb_back_to_categories
from random import randint


router = Router()
message = Message()
message.edit_reply_markup

@router.message(text=["Начать покупки"])
async def choose_category(message: Message):
    await message.answer("Выберите категорию товара", reply_markup=kb_back_to_menu())
    await message.answer( reply_markup=kb_choose_category())

@router.callback_query(Text(text_endswith="_category_choosed"))
async def choose_product(callback: CallbackQuery):
    category = callback.data.split("_category_choosed")[0]
    print(category)
    await callback.message.answer("Выберите товар", reply_markup=kb_choose_product(category))
