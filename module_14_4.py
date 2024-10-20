from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import crud_functions_1


api = '7394162589:AAGhNhFIqJJdBA-DHFBOF0scIFQSs2sDut8'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.add(button1)
kb.add(button2)
kb.add(button3)


kb_2 = InlineKeyboardMarkup()
inline_button_1 = InlineKeyboardButton('Product 1', callback_data="product_buying")
inline_button_2 = InlineKeyboardButton('Product 2', callback_data="product_buying")
inline_button_3 = InlineKeyboardButton('Product 3', callback_data="product_buying")
inline_button_4 = InlineKeyboardButton('Product 4', callback_data="product_buying")
kb_2.add(inline_button_1)
kb_2.add(inline_button_2)
kb_2.add(inline_button_3)
kb_2.add(inline_button_4)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    products = crud_functions_1.get_all_products()
    number = 1
    for i in products:
        await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        with open(f'{number}.jpg', "rb") as img:
            await message.answer_photo(img, f'Продукт {number}')
        number += 1
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
