from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


tasks = [
    {"id": 1, "title": "Create weekly progress reports for my group thesis", "done": False},
    {"id": 2, "title": "Check my email inbox", "done": True},
    {"id": 3, "title": "Search for tech-related internships ", "done": False}
]

app = FastAPI()

@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }


@app.get("/health")
async def status():
    return { "status": "ok" }


@app.get("/tasks")
async def get_tasks():
    return tasks


@app.get("/tasks/{id}")
async def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task

    return JSONResponse(
        status_code=404,
        content={"error": f"Task {id} not found"},
    )


@app.post("/tasks")
async def create_task(req: Request):
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
