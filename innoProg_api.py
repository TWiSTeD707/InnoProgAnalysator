# innoProg_api.py
import requests
import datetime

def get_innoProg_user_solutions(user_id):
    """Запрашивает подробную информацию о решениях пользователя InnoProg."""
    url = f"https://bot.innoprog.ru/dataset/detailed/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, успешен ли запрос
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации о решениях: {e}")
        return None

def get_innoProg_user_scores(user_id):
    """Запрашивает информацию о времени решения и оценках заданий пользователя."""
    url = f"https://bot.innoprog.ru/dataset/general/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации о оценках заданий: {e}")
        return None

def get_innoProg_task_description(task_id):
    """Запрашивает детальное описание задания по его ID."""
    url = f"https://api.innoprog.ru:3000/task/{task_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации о задании: {e}")
        return None

def format_datetime(timestamp):
    """Преобразует метку времени в формат "дд-мм-гггг чч:мм:сс"."""
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%d-%m-%Y %H:%M:%S")