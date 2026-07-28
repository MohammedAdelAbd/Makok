#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python manage.py'

echo "Running collectstatic..."
$RUN_MANAGE_PY collectstatic --no-input

echo "Running migrations..."
$RUN_MANAGE_PY migrate --no-input

echo "Starting Gunicorn..."
exec poetry run gunicorn makok_backend.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --threads 2 \
    --timeout 120
