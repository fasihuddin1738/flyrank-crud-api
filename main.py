# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse
# pyrefly: ignore [missing-import]
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str | None = None 

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Learn FastAPI", "done": False},
    {"id": 3, "title": "Complete Stage 2", "done": True}
]

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_all_tasks():
    return tasks 

@app.get("/tasks/{id}", responses={404: {"description": f"Task {id} not found"}})
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

@app.post("/tasks", responses={400: {"description": "Invalid input - Title is missing or empty"}})
def create_task(task_in: TaskCreate):
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