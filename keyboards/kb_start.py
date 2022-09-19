from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Начать покупки")
    kb.button(text="О магазине")
    kb.button(text="Техподдержка")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите дальнейшее действие")