from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData


async def set_button():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Робота деканату"),
                KeyboardButton(text="Розклад дзвінків"),
                KeyboardButton(text="Викладачі інфо")
            ],
            [
                KeyboardButton(text="Питання до адмінів"),
            ]
        ],
        resize_keyboard=True
    )
    return menu
