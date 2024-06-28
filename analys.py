# analys.py
import datetime
from collections import defaultdict

def analyze_user_data(solutions_data, scores_data):
    """Анализирует данные о решениях и оценках пользователя."""

    # 1. Общее количество решенных заданий
    total_tasks = len(solutions_data)

    # 2. Среднее время решения заданий
    total_time = 0
    for solution in solutions_data:
        time_object = datetime.datetime.strptime(solution['time'], "%d-%m-%Y %H:%M:%S")
        total_time += ((time_object.hour * 60 + time_object.minute) / 60)  # Время в минутах
    average_time = total_time / total_tasks if total_tasks else 0

    # 3. Средняя оценка сложности, выставленная пользователем
    total_user_difficulty = sum(score['real_points'] for score in scores_data)
    average_user_difficulty = total_user_difficulty / len(scores_data) if scores_data else 0

    # 4. Среднее отклонение от оценки сложности задания, выставленной преподавателем
    total_deviation = sum(score['real_points'] - score['points'] for score in scores_data)
    average_deviation = total_deviation / len(scores_data) if scores_data else 0

    return {
        "total_tasks": total_tasks,
        "average_time": average_time,
        "average_user_difficulty": average_user_difficulty,
        "average_deviation": average_deviation,
    }