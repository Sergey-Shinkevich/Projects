from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

all_products = get_all_products()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
button_4 = KeyboardButton(text='Регистрация')
kb.add(button_1)
kb.insert(button_2)
kb.insert(button_3)
kb.insert(button_4)

kb_inline = InlineKeyboardMarkup()
button_1_inline = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2_inline = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb_inline.add(button_1_inline)
kb_inline.add(button_2_inline)

kb_product = InlineKeyboardMarkup()
button_1_product = InlineKeyboardButton(text='Продукт #1', callback_data='product_buying')
button_2_product = InlineKeyboardButton(text='Продукт #2', callback_data='product_buying')
button_3_product = InlineKeyboardButton(text='Продукт #3', callback_data='product_buying')
button_4_product = InlineKeyboardButton(text='Продукт #4', callback_data='product_buying')
kb_product.add(button_1_product)
kb_product.add(button_2_product)
kb_product.add(button_3_product)
kb_product.add(button_4_product)

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb_inline)

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х Вес + 6.25 х Рост - 5 х Возраст + 5')
    await call.answer()
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State(1000)

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text) is False:
        await state.update_data(username=message.text)
        await message.answer('Введите свой e-mail:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await state.finish()
    await message.answer('Пользователь зарегистрирован', reply_markup=kb)

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    recomendation = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) +5
    await message.answer(recomendation)
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    j = 1
    for i in all_products:
        await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        with open(f'files/{j}.jpg', 'rb') as img:
            await message.answer_photo(img)
        j += 1
    await message.answer('Выберете продукт для покупки:', reply_markup=kb_product)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
