from aiogram import Router, F, types
import logging
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import Database
homework_router = Router()

database = Database("db.sqlite3")


class HomeworkForm(StatesGroup):
    name = State()
    number = State()
    content = State()

@homework_router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Отправить домашнее задание", callback_data="submit_homework"),
        ]]
    )
    await message.answer(
        "Привет! 📚\n"
        "Я бот для приёма домашних заданий.\n"
        "Нажмите кнопку ниже, чтобы отправить свою работу.",
        reply_markup=kb
    )

@homework_router.callback_query(F.data == "submit_homework")
async def submit_homework(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(HomeworkForm.name)
    await callback.message.answer("Введите ваше имя:")
    await callback.answer()


@homework_router.message(HomeworkForm.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(HomeworkForm.number)
    await message.answer("Введите номер домашнего задания (от 1 до 8):")


@homework_router.message(HomeworkForm.number, F.text.in_(["1", "2", "3", "4", "5", "6", "7", "8"]))
async def process_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(HomeworkForm.content)
    await message.answer("Отправьте файл с домашним заданием или ссылку на GitHub:")

@homework_router.message(HomeworkForm.content, F.text | F.document)
async def process_homework(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data["name"]
    number = data["number"]

    if message.document:
        content = f"Файл: {message.document.file_id}"
    else:
        content = message.text

    try:
        homework_data = {
            "name": name,
            "hw_number": number,
            "github": content
        }
        database.save_homework(homework_data)
        await state.clear()
        await message.answer("✅ Домашнее задание отправлено и сохранено в базе данных!")
    except Exception as e:
        await message.answer("❌ Произошла ошибка при сохранении задания. Попробуйте позже.")
        logging.error(f"Ошибка при сохранении домашнего задания: {e}")
