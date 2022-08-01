from loader import dp
from aiogram.types import Message
from keyboards.default import menu
from aiogram.dispatcher.filters import Command
from utils.utils import text


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Оберіть питання нижче",
    reply_markup=menu)

@dp.message_handler(text("Робота деканату"), content_types=['text'], state="*")
async def get_answ(message: Message):
    await message.answer(f'''Деканат ФКН 

📩 Пошта: csd@karazin.ua

⏰ Часи роботи:
      ▫️ Пн-Чт (8.30 - 17.00)
      ▫️ Пт (8.30 - 16.00)
      ▫️ Перерва (12.30 - 13.15)
      ▫️ Прийом студентів (9.30 - 10.30; 13.15 - 15.00)''')

#@dp.message_handler(Text(equals=["Робота деканату","Розклад дзвінків","Викладачі інфо"]))
#async def get_answ(message: Message()):

 #   elif message.text == "Розклад дзвінків":
  #      await message.photo('supportBot/files/Розклад_пар.jpg') 