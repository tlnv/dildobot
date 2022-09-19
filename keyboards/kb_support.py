from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def back() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Вернуться в главное меню")
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите дальнейшее действие")