from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import logging
from dotenv import load_dotenv
import os
from database import Database

load_dotenv()
token = os.getenv("BOT_TOKEN")

if not token:
    raise ValueError("Ошибка: BOT_TOKEN не найден в .env файле!")

bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

database = Database("db.sqlite3")

try:
    database.create_tables()
except Exception as e:
    logging.error(f"❌ Ошибка при создании таблиц: {e}")

logging.basicConfig(level=logging.INFO)

