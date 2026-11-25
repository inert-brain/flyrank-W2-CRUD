from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response


tasks = [
    {"id": 1, "title": "Create weekly progress reports for my group thesis", "done": False},
    {"id": 2, "title": "Check my email inbox", "done": True},
    {"id": 3, "title": "Search for tech-related internships ", "done": False}
]

app = FastAPI()

@app.get("/")
async def root():
    """Task info."""
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }


@app.get("/health")
async def status():
    """Server status."""
    return { "status": "ok" }


@app.get("/tasks")
async def get_tasks():
    """Lists all tasks."""
    return tasks


@app.get("/tasks/{id}")
async def get_task(id: int):
    """Lists a speific task by ID"""
    for task in tasks:
        if task["id"] == id:
            return task

    return JSONResponse(
        status_code=404,
        content={"error": f"Task {id} not found"},
    )


@app.post("/tasks",
status_code=201,
openapi_extra={
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "minLength": 1}
                    },
                    "required": ["title"],
                },
                "example": {"title": "Buy milk"},
            }
        },
    }
},)
async def create_task(req: Request):
    """Creates a new task."""
    body = await req.json()

    if not isinstance(body, dict):
        return JSONResponse(
            status_code=400,
            content={"error": "Request body must be a JSON object"},
        )

    title = body.get("title")

    if not isinstance(title, str) or not title.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Title must be a non-empty string"},
        )

    new_id = 0
    for task in tasks:
       new_id = max(task["id"], new_id)
    new_id += 1

    new_task = {"id": new_id, "title": title, "done": False}
    tasks.append(new_task)
    return JSONResponse(status_code=201, content = new_task)



@app.put(
    "/tasks/{id}",
    openapi_extra={
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string", "minLength": 1},
                            "done": {"type": "boolean"},
                        },
                        "anyOf": [
                            {"required": ["title"]},
                            {"required": ["done"]},
                        ],
                    },
                    "example": {"done": True},
                }
            },
        }
    },
)

async def update_task(id: int, req: Request):
    """Updates a task's title or done (completion status)."""
    try:
        body = await req.json()
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid request body"}
        )

    if not isinstance(body, dict):
        return JSONResponse(
            status_code=400,
            content={"error": "Request body must be a JSON object"},
        )

    title = body.get("title")
    done = body.get("done")

    if (not title) and (done is None):
        return JSONResponse(
            status_code=400,
            content={"error": "Request must contain either title (str) or done (bool)"},
        )

    if "title" in body and (not isinstance(title, str) or not title.strip()):
        return JSONResponse(
            status_code=400,
            content={"error": "Title must be a non-empty string"},
        )


    if "done" in body and not isinstance(done, bool):
        return JSONResponse(
            status_code=400,
            content={"error": "Done must be a non-empty boolean"},
        )


    for task in tasks:
        if task["id"] == id:
            if title:
                task["title"] = title
            if "done" in body:
                task["done"] = done
            new_task = task
            return JSONResponse(
                status_code=200,
                content = new_task
            )

    return JSONResponse(
        status_code=404,
        content={"error": "Unknown id"}
    )


@app.delete("/tasks/{id}")
async def delete_task(id: int):
    """Deletes a task."""
    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            return Response(status_code=204)

    return JSONResponse(
        status_code=404,
        content={"error": "Unknown id"}
    )
