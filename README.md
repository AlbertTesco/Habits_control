# Habits control
## Инструкции по запуску проекта
Шаги по запуску проекта:
- клонировать репозиторий при помощи команды git clone git@github.com:AlbertTesco/Django_DRF.git
- При помощи команды `docker compose up --build` соберите и запустите все сервисы 
- После успешного выполнения предыдущего шага, ваше приложение будет доступно по адресу http://localhost:8000/

## Конфигурация

### Переменные окружения

Для корректной работы приложения убедитесь, что вы сконфигурировали следующие переменные окружения:

#### Django

- `SECRET_KEY`: Секретный ключ Django

#### База данных PostgreSQL

- `POSTGRES_DB`: Имя базы данных PostgreSQL
- `POSTGRES_USER`: Имя пользователя PostgreSQL
- `POSTGRES_PASSWORD`: Пароль пользователя PostgreSQL

#### Telegram

- `TELEGRAM_TOKEN`: Токен для работы с Telegram API

### Пример файла .env

Вы можете создать файл `.env`, используя `.env.sample` в качестве шаблона. Заполните значения переменных окружения в соответствии с вашей конфигурацией.

```dotenv
# Пример .env

SECRET_KEY=mysecretkey

POSTGRES_DB=mydatabase
POSTGRES_USER=mydatabaseuser
POSTGRES_PASSWORD=mypassword

TELEGRAM_TOKEN=mytelegramtoken