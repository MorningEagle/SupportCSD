from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import menu


from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.reply(f"Привет, {message.from_user.full_name}!", reply_markup=menu.set_button)

