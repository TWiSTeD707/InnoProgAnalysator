# main.py
import requests
import datetime
import json
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from innoProg_api import get_innoProg_user_solutions, get_innoProg_user_scores, format_datetime, get_innoProg_task_description
from analys import analyze_user_data

BOT_TOKEN = "" #Test Token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # Create a regular keyboard
    keyboard.add(KeyboardButton("📊 Анализировать данные"))  # Add buttons
    keyboard.add(KeyboardButton("➡️ Перейти в ТГ канал"))
    await message.answer("Привет! 👋 Я помогу тебе проанализировать твои результаты на InnoProg.", reply_markup=keyboard)
@dp.message_handler(text="📊 Анализировать данные")
async def handle_analyse(message: types.Message):
    await message.answer("Введите ваш ID в системе INNOPROG\nПример: /statistics 123")
@dp.message_handler(text="➡️ Перейти в ТГ канал")
async def handle_tg_channel(message: types.Message):
    await message.answer("Перехожу в канал…", reply_markup=None)
    await message.answer(f"https://t.me/innoprog", reply_markup=None)

@dp.message_handler(commands=['statistics'])
async def handle_statistics(message: types.Message):
    args = message.get_args()
    if args:
        user_id = (args)
        solutions_data = get_innoProg_user_solutions(user_id)
        scores_data = get_innoProg_user_scores(user_id)
        if solutions_data and scores_data:
            analysis = analyze_user_data(solutions_data, scores_data)
            await message.answer(f"Статистика пользователя {user_id}:\n"
                                f"- Общее количество решенных заданий: {analysis['total_tasks']}\n"
                                f"- Среднее время решения заданий: {round(analysis['average_time'])} минут\n"  # Round to nearest whole number
                                f"- Средняя оценка сложности (реальные баллы): {round(analysis['average_user_difficulty'])}\n"  # Round to nearest whole number
                                f"- Среднее отклонение от оценки преподавателя: {round(analysis['average_deviation'])}")  # Round to nearest whole number
        else:
            await message.answer(f"Не удалось получить информацию о решениях для пользователя {user_id}.")
    else:
        await message.answer("Введите ID пользователя для получения статистики.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
