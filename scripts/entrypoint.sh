#!/bin/bash

# Остановка при любой ошибке
set -e

echo "Waiting for PostgreSQL..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"

# Применяем миграции
echo "Applying database migrations..."
python manage.py migrate --noinput

# Собираем статику
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Компилируем переводы
echo "Compiling translations..."
python manage.py compilemessages || echo "No messages to compile"

# Наполняем БД начальными данными
echo "Initializing data..."
python manage.py shell < scripts/init_data.py

# Запуск Gunicorn
echo "Starting Gunicorn..."
exec gunicorn ezoz_logistics.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
