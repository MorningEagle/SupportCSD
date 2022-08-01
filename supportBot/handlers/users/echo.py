from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.utils import text
from keyboards.inline.support import support_keyboard, support_callback
from keyboards.default.menu import set_button

from loader import dp, bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(text("Робота деканату"), content_types=['text'], state="*")
async def bot_echo(message: types.Message):
    await message.answer(f'''Деканат ФКН 

📩 Пошта: csd@karazin.ua

⏰ Часи роботи:
      ▫️ Пн-Чт (8.30 - 17.00)
      ▫️ Пт (8.30 - 16.00)
      ▫️ Перерва (12.30 - 13.15)
      ▫️ Прийом студентів (9.30 - 10.30; 13.15 - 15.00)''')


@dp.message_handler(text("Розклад дзвінків"), content_types=['text'], state="*")
async def bot_timetables(message: types.Message):
     with open('supportBot/files/Розклад_пар.jpg', 'rb') as pic:
        await message.answer_photo(pic)


@dp.message_handler(text("Викладачі інфо"), content_types=['text'], state="*")
async def bot_proffessor(message: types.Message):
    with open('supportBot/files/Викладачі.xlsx', 'rb') as doc:
        await message.answer_document(doc)


@dp.message_handler(text("Питання до адмінів"), content_types=['text'], state="*")
async def admin_answer(message: types.Message):
    texte = "Нажміть на кнопку нижче"
    keyboard = await support_keyboard(messages="one")
    await message.answer(texte, reply_markup=keyboard)

@dp.callback_query_handler(support_callback.filter(messages="one"))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get("user_id"))

    await call.message.answer("Надішліть ваше повідомлення")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)
   # await call.message.answer(reply_markup=set_button)

@dp.message_handler(state="wait_for_support_message", content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")

    await bot.send_message(second_id, 
    f"Вам повідомлення, нажміть на кнопку нижче")
    keyboard = await support_keyboard(messages="one" ,user_id=message.from_user.id)
    await message.copy_to(second_id, reply_markup=keyboard)
    await message.answer("Ви надіслали повідомлення!", reply_markup=set_button)
    await state.reset_state()
    

# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
#@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
#async def bot_echo_all(message: types.Message, state: FSMContext):
 #   state = await state.get_state()
  #  await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
   #                      f"\nСодержание сообщения:\n"
    #                     f"<code>{message}</code>")
