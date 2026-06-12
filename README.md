# Habit Tracker

Веб-приложение для отслеживания привычек на Flask.

## Установка

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python run.py
```

Открыть:

http://127.0.0.1:5000

## Тесты

Запуск тестов:

```bash
pytest
```

## Структура БД

### Habit

- id
- name
- description
- target_per_day

### Completion

- id
- habit_id
- completed_date