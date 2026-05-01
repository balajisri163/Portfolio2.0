#!/usr/bin/env bash
# Render build script
set -o errexit
set -o pipefail

echo "==> Python: $(python --version)"
echo "==> Pip: $(pip --version)"

echo "==> Installing dependencies"
pip install --upgrade pip
pip install -r requirements.txt

echo "==> Collecting static files"
python manage.py collectstatic --no-input

echo "==> Running migrations"
python manage.py migrate --no-input

echo "==> Build complete"