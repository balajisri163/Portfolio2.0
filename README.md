# Balaji Ramachandran — Portfolio

Personal portfolio website built with Django.

## Local development

```bash
python -m venv venv
venv/Scripts/activate     # Windows
# source venv/bin/activate  # macOS / Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Site runs at http://127.0.0.1:8000/.

## Deployment (Render)

The repo includes `render.yaml`, `build.sh`, and `Procfile`. On Render:

1. **New → Blueprint** → connect this repo.
2. Render reads `render.yaml`, generates a `DJANGO_SECRET_KEY`, and deploys.
3. Once live, add the deployed hostname (e.g. `balaji-portfolio.onrender.com`) to the `DJANGO_ALLOWED_HOSTS` env var if it isn't auto-detected.

Static files are served by WhiteNoise; `/media/` (resume PDF, photos) is also served via WhiteNoise from `media/`.

## Environment variables

| Var | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Secret key (auto-generated on Render) |
| `DJANGO_DEBUG` | `false` in production |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated host list |