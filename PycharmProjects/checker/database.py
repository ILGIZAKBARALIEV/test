import sqlite3
import logging


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS homework_submissions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        hw_number INTEGER NOT NULL,
                        github TEXT NOT NULL
                    )
                """)
                conn.commit()
                logging.info("Таблица homework_submissions успешно создана или уже существует.")
        except sqlite3.Error as e:
            logging.error(f"Ошибка при создании таблицы: {e}")

    def save_homework(self, data: dict):
        if not all(key in data for key in ["name", "hw_number", "github"]):
            logging.error("Ошибка: отсутствуют обязательные данные для сохранения домашки.")
            return

        try:
            hw_number = int(data["hw_number"])
            if hw_number not in range(1, 9):  # Проверка, чтобы номер задания был в пределах от 1 до 8
                logging.error("Ошибка: номер домашнего задания должен быть от 1 до 8.")
                return
            if not isinstance(data["name"], str) or not isinstance(data["github"], str):
                logging.error("Ошибка: поля 'name' и 'github' должны быть строками.")
                return

            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO homework_submissions (name, hw_number, github)
                    VALUES (?, ?, ?)
                """, (data["name"], hw_number, data["github"]))
                conn.commit()
                logging.info("Домашнее задание успешно сохранено.")
        except sqlite3.Error as e:
            logging.error(f"Ошибка при сохранении домашнего задания в базу: {e}")
        except ValueError as ve:
            logging.error(f"Ошибка преобразования данных: {ve}")
