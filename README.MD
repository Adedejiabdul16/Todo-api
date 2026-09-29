# Simple To-Do API

A simple to-do list REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite**, with interactive docs via Swagger UI and database migrations via Alembic.

## Features

- Create, read, update, and delete tasks
- Mark tasks as completed
- Interactive API docs (Swagger UI)
- SQLite database, no setup needed
- Alembic migrations

## Project structure

```
to do/
├── app/
│   ├── __init__.py
│   ├── database.py    # database connection and session
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas
│   └── main.py        # FastAPI app and routes
├── alembic/           # migration scripts
├── alembic.ini
├── requirements.txt
└── README.md
```

## Getting started

### 1. Clone the repo

```powershell
git clone https://github.com/YOUR-USERNAME/todo-api.git
cd todo-api
```

### 2. Create and activate a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Set up the database

```powershell
alembic upgrade head
```

### 5. Run the server

```powershell
uvicorn app.main:app --reload
```

The API runs at http://127.0.0.1:8000

## API docs

Open **http://127.0.0.1:8000/docs** for Swagger UI, where you can try every endpoint directly in the browser.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| POST | `/todos` | Create a task |
| GET | `/todos` | List all tasks |
| GET | `/todos/{id}` | Get one task |
| PUT | `/todos/{id}` | Update a task |
| DELETE | `/todos/{id}` | Delete a task |

### Example request

`POST /todos`

```json
{
  "title": "Buy groceries",
  "description": "Milk, bread, eggs"
}
```

## Database migrations

After changing `app/models.py`:

```powershell
alembic revision --autogenerate -m "describe your change"
alembic upgrade head
```

## Tech stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
- SQLite