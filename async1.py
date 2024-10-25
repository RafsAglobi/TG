from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

api = '7302950034:AAFWffsqRBTIK_rYt8z61htFdpmY2Txnq4s'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
b1 = KeyboardButton(text='Информация о боте')
b2 = KeyboardButton(text='Личный кабинет')
b3 = KeyboardButton(text='Подписки')

kb.add(b1)
kb.add(b2)
kb.add(b3)

kb_bot = InlineKeyboardMarkup()
b4 = InlineKeyboardButton(text='Сегодня', collback_date='дата')
b5 = InlineKeyboardButton(text='Завтра', callback_data='дата')

kb_bot.add(b4)
kb_bot.add(b5)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Выбери кнопку ниже:', reply_markup=kb)

@dp.message_handler(text=['дата'])
async def time_of_del(message):
    await message.answer('Выбери время доставки:', reply_markup=kb)


class UserState(StatesGroup):
    address = State()

@dp.message_handler(text=['заказать'])
async def delivery(message):
    await message.answer('Отправь свой адрес, пожалуйста')
    await UserState.address.set()

@dp.message_handler(state=UserState.address)
async def answer1(message, state):
    await state.update_date(first=message.text)
    data = await state.get_data()
    first = data['first']
    await message.answer(f'Супер! Доставка будет осуществлятся по адресу: {first}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

