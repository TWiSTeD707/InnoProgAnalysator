# analys.py - Анализ данных пользователей InnoProg

Этот модуль содержит функции для анализа данных пользователей InnoProg, собранных из API. Он вычисляет различные метрики, которые дают ценную информацию о производительности пользователя.

## Функции:

    analyze_user_data(solutions_data, scores_data): Основная функция, которая принимает два списка данных:
        solutions_data: Список подробной информации о решениях пользователя (получен из get_innoProg_user_solutions).
        scores_data: Список общей информации о оценках пользователя (получен из get_innoProg_user_scores).
    Функция анализирует данные и вычисляет следующие метрики:
        total_tasks: Общее количество решенных задач.
        average_time: Среднее время решения задач.
        average_user_difficulty: Средняя оценка сложности, выставленная пользователем.
        average_deviation: Среднее отклонение от оценки сложности задания, выставленной преподавателем.
        average_time_between_attempts: Среднее время между попытками решения.
        average_attempts_by_type: Среднее количество попыток для разных типов заданий (например, "С вариантами ответов", "Открытый вопрос").
        first_attempt_success_rate: Процент правильных ответов с первой попытки для заданий с вариантами ответов.
        success_rate: Общий процент успешных попыток.
    Функция возвращает словарь, содержащий все рассчитанные метрики.

## Использование:

    Импортируйте модуль: from analys import analyze_user_data

## Получите данные о решениях и оценках пользователя с помощью

solutions_data = get_innoProg_user_solutions(user_id)

scores_data = get_innoProg_user_scores(user_id)

## Вызовите функцию analyze_user_data с полученными данными:

analysis = analyze_user_data(solutions_data, scores_data)

## Доступ к рассчитанным метрикам можно получить через словарь analysis:

    print(f"Среднее время решения задач: {analysis['average_time']:.2f} секунд")
    print(f"Процент успешных попыток: {analysis['success_rate']:.2f}%")

# Пример:

from analys import analyze_user_data

# Пример данных (должны быть получены из API)
solutions_data = [
    {"time": 120, "task_id": 1},
    {"time": 240, "task_id": 2},
]
scores_data = [
    {"real_points": 3, "points": 3, "type": "С вариантами ответов", "attempts": 1},
    {"real_points": 2, "points": 3, "type": "Открытый вопрос", "attempts": 2},
]

analysis = analyze_user_data(solutions_data, scores_data)

print(analysis)

Дополнительные замечания:

    Этот модуль предназначен для использования в сочетании с main.py и innoProg_api.py
