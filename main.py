"""Main application for the Task API."""

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import task
import task_repository


app = FastAPI()
task_repo = task_repository.TaskRepository()

class TaskCreate(BaseModel):
    """Schema for creating a new task."""

    description: str

class TaskResponse(BaseModel):
    """Schema for task response."""

    id: int
    description: str
    completed: bool

@app.get("/tasks/", response_model=List[TaskResponse])
async def read_tasks():
    """Retrieve all tasks."""
    tasks_db = task_repo.get_all()
    response = []
    for task_db in tasks_db:
        response.append(
            TaskResponse(
                id=task_db['id'],
                description=task_db['description'],
                completed=task_db['completed']
            )
        )
    return response

@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int):
    """Retrieve a single task by ID."""
    task_db = task_repo.get_by_id(task_id)
    if task_db is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse(
        id=task_db['id'],
        description=task_db['description'],
        completed=task_db['completed']
    )

@app.post("/tasks/", response_model=TaskResponse, status_code=201)
async def create_task(task_create: TaskCreate):
    """Create a new task."""
    task_db = task_repo.get_all()
    ids = [t['id'] for t in task_db]
    task_id = max(ids) + 1 if ids else 1
    new_task = task.Task(task_id=task_id, description=task_create.description)
    task_repo.save(new_task)
    return TaskResponse(
        id=new_task.task_id,
        description=new_task.description,
        completed=new_task.completed)

@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, updated_task: TaskCreate):
    """Update an existing task."""
    task_db = task_repo.get_by_id(task_id)
    if task_db is None:
        raise HTTPException(status_code=404, detail="Task not found")

    new_task = task.Task(task_id=task_id, description=updated_task.description)
    task_repo.save(new_task)
    return TaskResponse(
        id=new_task.task_id,
        description=new_task.description,
        completed=new_task.completed)

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task by ID."""
    task_repo.delete(task_id)
    task_db = task_repo.get_by_id(task_id)
    if task_db is not None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success"}
