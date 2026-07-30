# Stage 0
# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Response
# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse
# pyrefly: ignore [missing-import]
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str | None = None 

class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Learn FastAPI", "done": False},
    {"id": 3, "title": "Complete Stage 2", "done": True}
]

# Stage 1
@app.get("/")
def read_root():
    """Returns API name and version."""
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health():
    """Checks if the server is alive."""
    return {"status": "ok"}

# Stage 2
@app.get("/tasks")
def get_all_tasks():
    """Returns a list of all tasks in the in-memory database."""
    return tasks 

@app.get("/tasks/{id}", responses={404: {"description": "Task not found"}})
def get_task(id: int):
    """Returns a single task matching the provided ID."""
    for task in tasks:
        if task["id"] == id:
            return task
    
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

# Stage 3
@app.post("/tasks", responses={400: {"description": "Invalid input - Title is missing or empty"}})
def create_task(task_in: TaskCreate):
    """Creates a new task and assigns it a unique ID."""
    if not task_in.title or not task_in.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title is missing or empty"})
    
    if len(tasks) > 0:
        next_id = max(task["id"] for task in tasks) + 1
    else:
        next_id = 1
    
    new_task = {
        "id": next_id,
        "title": task_in.title.strip(),
        "done": False
    }

    tasks.append(new_task)

    return JSONResponse(status_code=201, content=new_task)

# Stage 4
@app.put("/tasks/{id}" , responses={400: {"description": "Invalid body"}, 404: {"description": "Task not found"}})
def update_task(id: int, task_in: TaskUpdate):
    """Updates the title or completion status of an existing task."""
    if task_in.title is None and task_in.done is None:
        return JSONResponse(status_code=400, content={"error": "Body cannot be empty"})

    if task_in.title is not None and not task_in.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title cannot be empty"})
    
    for task in tasks:
        if task["id"] == id:
            if task_in.title is not None:
                task["title"] = task_in.title.strip()
            if task_in.done is not None:
                task["done"] = task_in.done
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

@app.delete("/tasks/{id}", responses={404: {"description": "Task not found"}})
def delete_task(id: int):
    """Deletes a task from the list based on its ID."""
    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            return Response(status_code = 204)
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})    
