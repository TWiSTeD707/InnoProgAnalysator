# innoProg_api.py - Взаимодействие с API InnoProg

## Этот модуль предоставляет функции для взаимодействия с API InnoProg, позволяя извлекать данные о пользователях и задачах. Он упрощает доступ к API, предоставляя удобные функции для запросов данных.

# Функции:

    get_innoProg_user_solutions(user_id): Возвращает подробную информацию о решениях пользователя InnoProg, включая время решения, тип задачи, количество попыток и другие детали.
    get_innoProg_user_scores(user_id): Возвращает общую информацию о результатах пользователя, включая время решения, реальную оценку, оценку преподавателя и тип задачи.
    get_innoProg_task_description(task_id): Возвращает детальное описание задачи по ее ID.
    format_datetime(timestamp): Форматирует метку времени в удобочитаемый формат "дд-мм-гггг чч:мм:сс".

# Использование:

    Импортируйте модуль: from innoProg_api import get_innoProg_user_solutions, get_innoProg_user_scores, format_datetime

## Вызовите функции для получения данных:

solutions_data = get_innoProg_user_solutions(user_id)
scores_data = get_innoProg_user_scores(user_id)
task_description = get_innoProg_task_description(task_id)

## Используйте полученные данные для дальнейшей обработки:

    print(f"Пользователь {user_id} решил {len(solutions_data)} задач.")
    print(f"Описание задачи {task_id}: {task_description['title']}")

# Пример:

from innoProg_api import get_innoProg_user_solutions, get_innoProg_user_scores, format_datetime

user_id = 12345  # Замените на реальный ID пользователя

solutions_data = get_innoProg_user_solutions(user_id)
scores_data = get_innoProg_user_scores(user_id)

if solutions_data and scores_data:
    print("Данные пользователя успешно получены.")
    for solution in solutions_data:
        print(f"Задача: {solution['task_id']}, Время решения: {format_datetime(solution['time'])}")
else:
    print("Ошибка получения данных.")

## Дополнительные замечания:

    Этот модуль требует установленных библиотек requests и datetime.
    Для использования API InnoProg необходимы соответствующие учетные данные (например, API-ключ).
    Документация API InnoProg доступна по адресу [ссылка на документацию API].

## Рекомендации:

    Используйте этот модуль для создания ботов, веб-приложений или других инструментов, взаимодействующих с данными InnoProg.
    Подробно изучите API InnoProg, чтобы использовать все его возможности.
    Следуйте рекомендациям по использованию API, чтобы обеспечить его стабильную работу и избежать ошибок.
