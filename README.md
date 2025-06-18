# stonechat_frontend

Минималистичный фронтенд для группового чата через WebSocket.

## Возможности
- Веб-интерфейс для группового чата
- Подключение к WebSocket серверу (требуется backend)
- Авторизация через Google (JWT-токен)
- Простая интеграция с backend-проектом [requp/stonechat](https://github.com/requp/stonechat)

## Требования
- Python 3.10+
- Установленные зависимости из `requirements.txt`

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/requp/stonechat_frontend.git
   cd stonechat_frontend
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Настройка
1. Скопируйте пример файла переменных окружения:
   ```bash
   cp .example.env .env
   ```
2. Отредактируйте `.env` под свои нужды:
   ```env
   MODE=DEV
   UVICORN_PORT=8000
   UVICORN_HOST=0.0.0.0
   PROD_HOST=your.prod
   PROD_PORT=8000
   BACKEND_API_V1_URL=http://localhost:8000/api/v1
   ```
   - `BACKEND_API_V1_URL` — URL backend-сервера (например, [requp/stonechat](https://github.com/requp/stonechat)), который реализует WebSocket-чат и авторизацию.

## Запуск
```bash
python app/main.py
```

Или через uvicorn напрямую:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Использование
- Перейдите в браузере по адресу: `http://localhost:8000/chat/simple_group_chat/{token}`
- `{token}` — JWT-токен, полученный после авторизации через backend (Google OAuth).
- Интерфейс позволяет отправлять и получать сообщения в реальном времени.

## Важно
- Для работы чата необходим backend-сервер, реализующий WebSocket-логику и авторизацию пользователей. Рекомендуется использовать [requp/stonechat](https://github.com/requp/stonechat).
- Данный проект — только frontend-часть!

## Ссылки
- Основной backend-проект: [requp/stonechat](https://github.com/requp/stonechat)
