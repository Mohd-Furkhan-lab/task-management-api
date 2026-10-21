# Task Management API

A RESTful task manager built with **FastAPI** and **SQLAlchemy**. Users sign up, log in to receive a **JWT**, and then create, list, filter, update and delete their own tasks. Every task is private to the user who created it.

The project is structured as a layered architecture (**Routes → Controllers → Services → Database**) to practice clean backend design and token-based authentication.

---

## Features

- **User accounts:** signup and login with bcrypt-hashed passwords
- **JWT authentication:** stateless bearer tokens that expire after 1 hour
- **Per-user tasks:** each user only ever sees and modifies their own tasks
- **Full task lifecycle:** create, list, update status and delete
- **Filter by state:** fetch only the tasks in a given state (for example `pending` or `done`)
- **Reusable auth decorator:** a single `@jwt_required` decorator protects any route
- **Interactive docs:** Swagger UI and ReDoc generated automatically
- **Zero-setup database:** SQLite file created locally, with no server to install

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | FastAPI + Uvicorn |
| ORM / database | SQLAlchemy 2.0 + SQLite |
| Authentication | PyJWT (HS256) |
| Password hashing | bcrypt |
| Validation / typing | Pydantic v2 (via FastAPI) |

## Architecture

```text
Request
   │
   ▼
Routes         → define URLs, apply @jwt_required
   │
   ▼
Controllers    → read the request, extract user_id and body
   │
   ▼
Services       → business logic (hashing, token creation, task rules)
   │
   ▼
Database       → SQLAlchemy models and queries
```

## Project Structure

```text
task-management-api/
├── app/
│   └── main.py                 # FastAPI app, CORS, router registration
├── routes/
│   ├── users.py                # /users endpoints
│   └── tasks.py                # /tasks endpoints
├── controller/
│   ├── user_controller.py
│   └── task_controller.py
├── services/
│   ├── user_services.py        # signup, login, token creation
│   └── task_services.py        # task operations
├── database/
│   ├── db.py                   # engine, session factory, Base
│   ├── user_model.py           # User table + queries
│   └── tasks_model.py          # Task table + queries
├── middelware/
│   ├── jwt.py                  # create / verify JWTs
│   └── jwt_decorator.py        # @jwt_required route guard
├── init_db.py                  # creates the database tables
├── run.py                      # Uvicorn entrypoint (exposes `app`)
├── requirements.txt
└── Readme.md
```

## Getting Started

### Prerequisites

- Python **3.10+**

### 1. Clone

```bash
git clone https://github.com/Mohd-Furkhan-lab/task-management-api.git
cd task-management-api
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### 3. Create the database tables

```bash
python init_db.py
```

This creates a local `Tasks.db` SQLite file with the `users` and `tasks` tables. Run it once before starting the server.

### 4. Start the server

```bash
uvicorn run:app --reload
```

The API is now available at `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Authentication

1. Create an account with `POST /users/signup`.
2. Log in with `POST /users/login`. The response body is your **JWT**.
3. Send it on every task request in the `Authorization` header:

```http
Authorization: Bearer <your_token>
```

Tokens carry the user's ID and expire **1 hour** after login. Requests with a missing, invalid or expired token receive `401 Unauthorized`.

> **Note:** the task routes are protected by a custom decorator, so Swagger UI has no "Authorize" button for them. Test protected endpoints with `curl`, Postman or any HTTP client that lets you set headers.

## API Reference

### Users

| Method | Endpoint | Body | Description |
|---|---|---|---|
| `POST` | `/users/signup` | `name`, `email`, `password` | Register a new user. |
| `POST` | `/users/login` | `name`, `password` | Log in and receive a JWT. |

**Signup**

```json
{
  "name": "furkhan",
  "email": "furkhan@example.com",
  "password": "your-password"
}
```

**Login**

```json
{
  "name": "furkhan",
  "password": "your-password"
}
```

Login accepts the account **name** (not the email).

### Tasks 🔒

All task endpoints require the `Authorization: Bearer <token>` header.

| Method | Endpoint | Body | Description |
|---|---|---|---|
| `GET` | `/tasks/` | none | List all your tasks. |
| `GET` | `/tasks/?state=done` | none | List only tasks whose state matches. |
| `POST` | `/tasks/` | `task`, `state` | Create a task. |
| `PUT` | `/tasks/{id}` | `state` | Update a task's state. |
| `DELETE` | `/tasks/{id}` | none | Delete a task. |

**Create a task**

```json
{
  "task": "Write the project README",
  "state": "pending"
}
```

**Update a task**

```json
{
  "state": "done"
}
```

**List response**

```json
{
  "data": [
    { "id": 1, "user_id": 1, "task": "Write the project README", "state": "done" }
  ]
}
```

`state` is a free-form string, so you can use whatever workflow suits you, for example `pending`, `in-progress` and `done`.

## Example Usage (curl)

```bash
# 1. Sign up
curl -X POST http://127.0.0.1:8000/users/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "furkhan", "email": "furkhan@example.com", "password": "secret123"}'

# 2. Log in (the response is your token)
curl -X POST http://127.0.0.1:8000/users/login \
  -H "Content-Type: application/json" \
  -d '{"name": "furkhan", "password": "secret123"}'

# 3. Create a task
curl -X POST http://127.0.0.1:8000/tasks/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"task": "Write the README", "state": "pending"}'

# 4. List your tasks, then only the pending ones
curl http://127.0.0.1:8000/tasks/ -H "Authorization: Bearer <token>"
curl "http://127.0.0.1:8000/tasks/?state=pending" -H "Authorization: Bearer <token>"

# 5. Mark task 1 as done
curl -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"state": "done"}'

# 6. Delete task 1
curl -X DELETE http://127.0.0.1:8000/tasks/1 -H "Authorization: Bearer <token>"
```

## Data Model

| Table | Columns |
|---|---|
| `users` | `id` (PK), `name`, `email`, `password` (bcrypt hash) |
| `tasks` | `id` (PK), `user_id`, `task`, `state` |

## Before You Deploy

This project is built for learning, so a few things should change before it faces real users:

- **Move the JWT secret out of the code.** `SECRET_KEY` is currently set in `middelware/jwt.py`. Load it from an environment variable and use a fresh random value.
- **Restrict CORS.** `app/main.py` currently allows requests from any origin.
- **Use a production database** such as PostgreSQL instead of the local SQLite file.

## Roadmap Ideas

- Enforce unique usernames and emails
- Return proper HTTP status codes for errors such as a wrong password
- Validate request bodies with Pydantic models and restrict `state` to a fixed set of values
- Return `404` when updating or deleting a task that does not exist
- Add task due dates, priorities and descriptions
- Add automated tests

## Contributing

Issues and pull requests are welcome. Please open a branch and describe the change clearly.

## License

No license file is included yet. Add one (for example MIT) to define how others may use this code.
