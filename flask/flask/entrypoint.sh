#!/bin/bash

APP_HOST=0.0.0.0
APP_PORT=5001
APP_WORKERS=2

echo -e "=====Start application server at http://${APP_HOST}:${APP_PORT} with ${APP_WORKERS} workers====="

gunicorn -b $APP_HOST:$APP_PORT -w=$APP_WORKERS wsgi:app
