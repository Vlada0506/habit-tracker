# Архитектура проекта

## Flask

Используется фабрика приложений:

create_app()

## База данных

SQLite + SQLAlchemy

Таблицы:

### Habit

- id
- name
- description
- target_per_day

### Completion

- id
- habit_id
- completed_date

Связь:

Habit 1 -> N Completion

## Маршруты

/ - список привычек

/add - создание

/habit/<id> - просмотр истории

/toggle/<id> - отметить выполнение

/edit/<id> - редактирование

/delete/<id> - удаление

/search - поиск