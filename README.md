# Travelover Pro

## Описание

**Travelover Pro** — это Telegram-бот для безопасных сделок (эскроу) между пользователями, с возможностью пополнения и вывода средств, ведением истории сделок, рейтингов и профилей. Проект использует асинхронный Python-стек (aiogram, SQLAlchemy, asyncpg), хранит данные в PostgreSQL и Redis, поддерживает миграции через Alembic и полностью контейнеризован с помощью Docker.

## Основные возможности

- Регистрация и авторизация пользователей через Telegram
- Эскроу-сделки между пользователями (создание, подтверждение, арбитраж)
- Пополнение и вывод средств (USDT TRC20, LTC, BTC, TON)
- Рейтинги и история сделок
- Админ-панель (через Telegram)
- Хранение данных в PostgreSQL, кэширование и FSM — в Redis

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone <URL-репозитория>
cd <имя-папки>
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта и заполните его по примеру:

```
BOT_TOKEN=ваш_токен_бота
ADMIN=ваш_telegram_id

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=пароль
POSTGRES_DB=travelover

ADMIN_IDS=список_id_админов_через_запятую

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=пароль
```

### 3. Запуск через Docker Compose

```bash
docker-compose up --build
```

Это поднимет контейнеры с PostgreSQL, Redis и самим ботом.

### 4. Локальный запуск (без Docker)

1. Установите зависимости:
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
2. Запустите миграции БД:
    ```bash
    alembic upgrade head
    ```
3. Запустите бота:
    ```bash
    python main.py
    ```

## Миграции базы данных

Для управления схемой БД используется Alembic:

- Создать новую миграцию:
    ```bash
    alembic revision --autogenerate -m "описание"
    ```
- Применить миграции:
    ```bash
    alembic upgrade head
    ```

## Зависимости

- Python 3.11+
- aiogram 3.x
- SQLAlchemy 2.x
- asyncpg, alembic, redis, environs и др. (см. `requirements.txt`)

## Структура проекта

- `main.py` — точка входа, инициализация бота
- `handlers.py` — обработчики команд и логика FSM
- `database/` — модели, миграции, работа с БД
- `config_data/` — конфигурация и работа с переменными окружения
- `keybords/` — клавиатуры Telegram
- `functions.py` — вспомогательные функции

## Контакты

Для связи с администратором используйте Telegram: [@Yacobovitz](https://t.me/Skydive_m) 