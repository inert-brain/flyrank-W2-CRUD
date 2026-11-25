# Task API

A FastAPI to-do list API for creating, listing, updating, and deleting tasks. Tasks are stored in memory. Restarting the server restores the three sample tasks.

## Install and run

From the repository root, set up a virtual environment in Bash. This project was tested with Python 3.15.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install fastapi==0.165.0 uvicorn==0.54.0
```

Start the server with:

```bash
python -m uvicorn main:app --port 3000
```

Open [http://localhost:3000/health](http://localhost:3000/health) to check that the server is running.

## Endpoints

| Method | Path | Description | Success |
| --- | --- | --- | --- |
| GET | `/` | Get the API name, version, and task path | `200 OK` |
| GET | `/health` | Check that the server is running | `200 OK` |
| GET | `/tasks` | List all tasks | `200 OK` |
| GET | `/tasks/{id}` | Get a task by ID | `200 OK` |
| POST | `/tasks` | Create a task from a JSON body with a `title` | `201 Created` |
| PUT | `/tasks/{id}` | Update a task's `title`, `done`, or both | `200 OK` |
| DELETE | `/tasks/{id}` | Remove a task by ID | `204 No Content` |
| GET | `/docs` | Open the interactive Swagger UI | `200 OK` |
| GET | `/redoc` | Open the ReDoc API reference | `200 OK` |
| GET | `/openapi.json` | Get the generated OpenAPI schema | `200 OK` |

## curl example

In a second terminal, list the tasks:

```bash
curl -i http://localhost:3000/tasks
```

Output captured after deleting the test task:

```http
HTTP/1.1 200 OK
date: Wed, 25 Nov 2026 16:04:00 GMT
server: uvicorn
content-length: 205
content-type: application/json

[{"id":1,"title":"Create weekly progress reports for my group thesis","done":false},{"id":2,"title":"Check my email inbox","done":true},{"id":3,"title":"Search for tech-related internships ","done":false}]
```

## Swagger UI

With the server running, open [Swagger UI](http://localhost:3000/docs).

Use **Try it out** on `POST /tasks` to create a task, then use `GET /tasks`
to find it. Use the ID returned by POST to update the task with
`PUT /tasks/{id}` and remove it with `DELETE /tasks/{id}`.

![Swagger UI showing the task creation response](screenshots/Screenshot%20From%202026-11-26%2000-30-25.png)

| Endpoint | Screenshots |
| --- | --- |
| `GET /` | [API information](screenshots/Screenshot%20From%202026-11-26%2000-29-37.png) |
| `GET /health` | [Health check](screenshots/Screenshot%20From%202026-11-26%2000-29-56.png) |
| `GET /tasks` | [Task list](screenshots/Screenshot%20From%202026-11-26%2000-30-05.png) |
| `POST /tasks` | [Request](screenshots/Screenshot%20From%202026-11-26%2000-30-16.png), [response](screenshots/Screenshot%20From%202026-11-26%2000-30-25.png) |
| `GET /tasks/{id}` | [Task details](screenshots/Screenshot%20From%202026-11-26%2000-30-33.png) |
| `PUT /tasks/{id}` | [Request](screenshots/Screenshot%20From%202026-11-26%2000-30-39.png), [response](screenshots/Screenshot%20From%202026-11-26%2000-30-45.png) |
| `DELETE /tasks/{id}` | [Delete response](screenshots/Screenshot%20From%202026-11-26%2000-31-40.png), [repeat request](screenshots/Screenshot%20From%202026-11-26%2000-32-04.png) |
