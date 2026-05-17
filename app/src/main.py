import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pythonjsonlogger import jsonlogger
from pydantic import BaseModel

# Structured JSON logging — required for Loki to parse logs correctly
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(jsonlogger.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(name)s %(message)s"
))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


# Data model — Pydantic validates incoming data automatically
class Task(BaseModel):
    id: int | None = None
    title: str
    done: bool = False


# In-memory storage — simple for now, database comes later
tasks: list[Task] = []
task_counter = 0


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting cloud-gitops-platform API")
    yield
    logger.info("Shutting down cloud-gitops-platform API")


app = FastAPI(
    title="Cloud GitOps Platform API",
    description="Task management API — DevSecOps portfolio project",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    """Health check endpoint — used by Kubernetes readiness probe."""
    logger.info("Health check requested")
    return {"status": "ok", "version": "0.1.0"}


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    """Return all tasks."""
    logger.info("Fetching all tasks", extra={"count": len(tasks)})
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    """Create a new task."""
    global task_counter
    task_counter += 1
    task.id = task_counter
    tasks.append(task)
    logger.info("Task created", extra={"task_id": task.id, "title": task.title})
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Return a single task by ID."""
    for task in tasks:
        if task.id == task_id:
            return task
    logger.warning("Task not found", extra={"task_id": task_id})
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """Delete a task by ID."""
    global tasks
    original_count = len(tasks)
    tasks = [t for t in tasks if t.id != task_id]
    if len(tasks) == original_count:
        raise HTTPException(status_code=404, detail="Task not found")
    logger.info("Task deleted", extra={"task_id": task_id})
