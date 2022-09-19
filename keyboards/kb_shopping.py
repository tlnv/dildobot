from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import db


def kb_back_to_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Вернуться в главное меню")
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите дальнейшее действие")


def kb_back_to_categories() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Вернуться к категориям")
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите дальнейшее действие")


def kb_choose_category() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for category in db.categories:
        kb.add(InlineKeyboardButton(text=category,
               callback_data=f"{category}_category_choosed"))
    kb.adjust(1)
    kb.button(text="Вернуться в главное меню")
    return kb.as_markup()


def kb_choose_product(category) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for product in db.products[category]:
        kb.add(InlineKeyboardButton(text=product,
               callback_data=f"{product}_product_choosed"))
    kb.adjust(1)
    return kb.as_markup()
