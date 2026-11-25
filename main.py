from fastapi import FastAPI
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
