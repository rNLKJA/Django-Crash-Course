<div align="center">

# Django Crash Course — Storefront

Learning build of a Django **storefront** project, following Mosh Hamedani's "Python Django Tutorial for Beginners" crash course.

[![Django](https://img.shields.io/badge/Django-5.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue)](LICENSE)
![Status](https://img.shields.io/badge/status-learning_build-orange)

</div>

## Overview

This repository is a hands-on learning project, not a finished product. It follows
Mosh Hamedani's introductory Django crash course
([video](https://www.youtube.com/watch?v=rHux0gMZ3Eg)) to scaffold a `storefront`
project, and is kept as a personal reference for Django's core building blocks —
projects vs apps, URL routing, views, templates, and the development setup.

The codebase is an early checkpoint of the course. The `playground` app is wired up
end to end (a route, a view, and a template), while the `store` and `tag` apps are
freshly scaffolded placeholders waiting for their models and views.

## What's working

- **Project scaffolding** — a `storefront` Django project with `playground`, `store`,
  and `tag` apps registered.
- **Routing** — the project URLconf includes the `playground` app's routes and the
  Django Debug Toolbar ([`storefront/urls.py`](storefront/urls.py),
  [`playground/urls.py`](playground/urls.py)).
- **A working view + template** — `say_hello` renders `hello.html`, which greets the
  visitor by name or falls back to "Hello World"
  ([`playground/views.py`](playground/views.py),
  [`playground/templates/hello.html`](playground/templates/hello.html)).
- **Dev tooling** — Django Debug Toolbar configured for local development, plus a
  VS Code launch config that runs the dev server on port 9000.

## Still to do (tutorial in progress)

- `store` and `tag` apps have empty `models.py` and `views.py` — the product and
  collection data model (`Product`: title, description, price, inventory;
  `Collection`: title) is the next step in the course.
- No migrations have been created yet, and there is no `requirements.txt`.

## Tech stack

| Layer      | Tools                                   |
| ---------- | --------------------------------------- |
| Framework  | Django 5.1                              |
| Language   | Python 3.12                             |
| Database   | SQLite (development default)            |
| Templating | Django templates                        |
| Dev tools  | Django Debug Toolbar, VS Code (debugpy) |

## Getting started

> Requires Python 3.12+ and Git.

```bash
# 1. Clone the repository
git clone https://github.com/rNLKJA/Django-Crash-Course.git
cd Django-Crash-Course

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install Django and the Debug Toolbar
pip install "django>=5.1" django-debug-toolbar

# 4. Apply the built-in migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Then open <http://127.0.0.1:8000/playground/hello/> to see the greeting page.

> **Heads-up:** `INSTALLED_APPS` in [`storefront/settings.py`](storefront/settings.py)
> currently lists `tags` (the app is named `tag`) and includes `debug_toolbar` twice.
> If you hit an app-loading error on first run, that is the place to look — these are
> left as-is to reflect the tutorial checkpoint faithfully.

## Project layout

```
Django-Crash-Course/
├── manage.py              # Django management entry point
├── storefront/            # Project package (settings, URLs, WSGI/ASGI)
├── playground/            # Demo app — working route, view, and template
├── store/                 # Stub app — models/views to come
└── tag/                   # Stub app — models/views to come
```

## Credits

Built by following Mosh Hamedani's
[Python Django Tutorial for Beginners](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
(Code with Mosh). This repo is for learning only.

---

The original course README is preserved at
[`_archive/README.original.md`](_archive/README.original.md).
