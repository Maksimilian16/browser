from aiogram import types
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def reply_builder(buttons):
    kb = [[types.KeyboardButton(text=i)] for i in buttons]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="None"
    )
    return keyboard


def inline_builder(buttons):
    builder = InlineKeyboardBuilder()
    for value in buttons:
        builder.add(InlineKeyboardButton(text=value, callback_data=f"{value}/"))
    return builder.as_markup()
