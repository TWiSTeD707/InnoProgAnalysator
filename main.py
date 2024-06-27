# main.py
import requests
import datetime
import json
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from innoProg_api import get_innoProg_user_solutions, get_innoProg_user_scores, format_datetime, get_innoProg_task_description
from analys import analyze_user_data

BOT_TOKEN = "7445941676:AAHBb6q_AxLQcCx80I6PmR9uvRuBxFsi9PI" #Test Token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! 👋 Я помогу тебе проанализировать твои результаты на InnoProg. \nИспользуйте команду /statistics {user_id} для получения статистики.")

@dp.message_handler(commands=['statistics'])
async def handle_statistics(message: types.Message):
    try:
        args = message.get_args()
        if args:
            user_id = int(args)
            solutions_data = get_innoProg_user_solutions(user_id)
            scores_data = get_innoProg_user_scores(user_id)
            if solutions_data and scores_data:
                analysis = analyze_user_data(solutions_data, scores_data)
                await message.answer(f"Статистика пользователя {user_id}:\n"
                                    f"- Общее количество решенных заданий: {analysis['total_tasks']}\n"
                                    f"- Среднее время решения заданий: {analysis['average_time']:.2f} секунд\n"
                                    f"- Средняя оценка сложности (реальные баллы): {analysis['average_user_difficulty']:.2f}\n"
                                    f"- Среднее отклонение от оценки преподавателя: {analysis['average_deviation']:.2f}\n"
                                    f"- Среднее время между попытками решения: {analysis['average_time_between_attempts']:.2f} секунд\n"
                                    f"- Среднее количество попыток для заданий:\n"
                                    f"  - С вариантами ответов: {analysis['average_attempts_by_type']['С вариантами ответов']:.2f}\n"
                                    f"  - Открытый вопрос: {analysis['average_attempts_by_type']['Открытый вопрос']:.2f}\n"
                                    f"  - Написание кода: {analysis['average_attempts_by_type']['Написание кода']:.2f}\n"
                                    f"  - Дополнение кода: {analysis['average_attempts_by_type']['Дополнение кода']:.2f}\n"
                                    f"- Процент правильных ответов с первой попытки для заданий с вариантами ответов: {analysis['first_attempt_success_rate']:.2f}%\n"
                                    f"- Процент успешных попыток: {analysis['success_rate']:.2f}%")
            else:
                await message.answer(f"Не удалось получить информацию о решениях для пользователя {user_id}.")
        else:
            await message.answer("Введите ID пользователя для получения статистики.")

    except ValueError:
        await message.answer("Некорректный ID пользователя. Введите целое число.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
