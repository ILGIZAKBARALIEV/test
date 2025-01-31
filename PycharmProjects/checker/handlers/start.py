from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Отправить домашнее задание", callback_data="submit_homework"),
            ],
        ]
    )
    await message.answer(
        "Привет! 📚\n"
        "Я бот для приёма домашних заданий.\n"
        "Нажмите кнопку ниже, чтобы отправить свою работу.",
        reply_markup=kb
    )

@start_router.callback_query(F.data == "submit_homework")
async def submit_homework(callback: types.CallbackQuery):
    await callback.message.answer("Пожалуйста, отправьте файл или текст с вашим домашним заданием.")
