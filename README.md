# Бот для статистики InnoProg

## Этот репозиторий содержит код для бота Telegram, который анализирует статистику пользователей InnoProg. Бот получает данные пользователей из API InnoProg и предоставляет полезную информацию об их результатах.

# Возможности:

    Статистика пользователей: Собирает и анализирует данные пользователей, включая:
        Общее количество решенных задач
        Среднее время решения задач
        Среднюю оценку сложности, выставленную пользователем
        Среднее отклонение от оценки сложности задания, выставленной преподавателем
        Среднее время между попытками (в будущем)
        Среднее количество попыток для разных типов заданий (в будущем)
        Процент успешных ответов с первой попытки для заданий с вариантами ответов
        Общий процент успешных попыток
    Управление командами: Использует команды Telegram для взаимодействия.
        /start: Приветствует пользователя и дает инструкции.
        /statistics {user_id}: Извлекает и отображает статистику для указанного ID пользователя.

# Как использовать:

    Получите токен бота Telegram от BotFather.
    Замените заполнитель BOT_TOKEN на ваш токен бота.
    Запустите бота с помощью python main.py.
    Начните разговор с вашим ботом в Telegram.
    Используйте команду /statistics, за которой следует ID пользователя, чтобы получить его статистику.

# Структура кода:

## Основная логика бота, включая настройку бота Telegram, обработчики команд и получение/отображение статистики.
## Функции для взаимодействия с API InnoProg для получения данных пользователей.

    Функции для анализа данных пользователей и расчета соответствующей статистики.

# Требования:

    Python 3.10 или выше
    aiogram
    requests

# Установка:

pip install -r requirements.txt

# Помочь проекту:

Ваша помощь приветствуется! Не стесняйтесь отправлять запросы на включение изменений или создавать проблемы.

Лицензия:

Этот проект лицензирован по лицензии MIT.

Примечание: Этот бот требует доступа к API InnoProg. Убедитесь, что у вас есть необходимые разрешения и учетные данные, прежде чем использовать его.
