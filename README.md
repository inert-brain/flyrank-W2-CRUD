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
