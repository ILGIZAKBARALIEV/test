import asyncio
import logging
from aiogram import Bot
from config import bot, dp, Database
from handlers import (homework,start)


async def on_startup():
    try:
        Database.create_tables()
        logging.info("✅ Таблицы успешно созданы.")
    except Exception as e:
        logging.error(f"❌ Ошибка при создании таблиц: {e}")


async def main():
    try:
        logging.info("🚀 Запуск бота...")


        dp.include_router(homework.homework_router)
        dp.include_router(start.start_router)


        await on_startup()

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except Exception as e:
        logging.error(f"❌ Ошибка при запуске бота: {e}")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("🛑 Бот остановлен вручную.")
