# analys.py
import datetime
from collections import defaultdict

def analyze_user_data(solutions_data, scores_data):
    """Анализирует данные о решениях и оценках пользователя."""

    # 1. Общее количество решенных заданий
    total_tasks = len(solutions_data)

    # 2. Среднее время решения заданий
    total_time = sum(int(solution['time']) for solution in solutions_data)
    average_time = total_time / total_tasks if total_tasks else 0

    # 3. Средняя оценка сложности, выставленная пользователем
    total_user_difficulty = sum(score['real_points'] for score in scores_data)
    average_user_difficulty = total_user_difficulty / len(scores_data) if scores_data else 0

    # 4. Среднее отклонение от оценки сложности задания, выставленной преподавателем
    total_deviation = sum(score['real_points'] - score['points'] for score in scores_data)
    average_deviation = total_deviation / len(scores_data) if scores_data else 0

    # 5. Среднее время между попытками решения
    attempts_times = []
    for score in scores_data:
        if score['attempts'] > 1:
            attempts_times.extend(score['time'] for _ in range(score['attempts'] - 1))
    average_time_between_attempts = sum(attempts_times) / len(attempts_times) if attempts_times else 0

    # 6. Среднее количество попыток решения для каждого типа заданий
    task_type_attempts = defaultdict(list)
    for score in scores_data:
        task_type_attempts[score['type']].append(score['attempts'])
    average_attempts_by_type = {
        task_type: sum(attempts) / len(attempts) if attempts else 0
        for task_type, attempts in task_type_attempts.items()
    }

    # 7. Процент правильных ответов с первой попытки для заданий с вариантами ответов
    correct_first_attempts = 0
    total_choice_tasks = 0
    for score in scores_data:
        if score['type'] == "С вариантами ответов":
            total_choice_tasks += 1
            if score['attempts'] == 1 and score['real_points'] == score['points']:
                correct_first_attempts += 1
    first_attempt_success_rate = (correct_first_attempts / total_choice_tasks) * 100 if total_choice_tasks else 0

    # 8. Дополнительный показатель: Процент заданий с успешной попыткой (реальная оценка = полная)
    successful_attempts = 0
    for score in scores_data:
        if score['real_points'] == score['points']:
            successful_attempts += 1
    success_rate = (successful_attempts / len(scores_data)) * 100 if scores_data else 0

    return {
        "total_tasks": total_tasks,
        "average_time": average_time,
        "average_user_difficulty": average_user_difficulty,
        "average_deviation": average_deviation,
        "average_time_between_attempts": average_time_between_attempts,
        "average_attempts_by_type": average_attempts_by_type,
        "first_attempt_success_rate": first_attempt_success_rate,
        "success_rate": success_rate,
    }