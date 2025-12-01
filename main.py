from fastapi import FastAPI, HTTPException
from typing import List, Optional
import Task
import TaskRepository

app = FastAPI()
task_repo = TaskRepository.TaskRepository()

from pydantic import BaseModel

class TaskCreate(BaseModel):
    description: str

class TaskResponse(BaseModel):
    id: int
    description: str
    completed: bool

@app.get("/tasks/", response_model=List[TaskResponse])
async def read_tasks():
    tasks_db = task_repo.get_all()
    response = []
    for task_db in tasks_db:
        response.append(TaskResponse(id=task_db['id'], description=task_db['description'], completed=task_db['completed']))
    return response

@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int):
    task_db = task_repo.get_by_id(task_id)
    if task_db is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse(id=task_db['id'], description=task_db['description'], completed=task_db['completed'])

@app.post("/tasks/", response_model=TaskResponse, status_code=201)
async def create_task(task_create: TaskCreate):
    task_db = task_repo.get_all()
    ids = [t['id'] for t in task_db]
    task_id = max(ids) + 1 if ids else 1
    
    task = Task.Task(id=task_id, description=task_create.description)
    task_repo.save(task)
    
    return TaskResponse(id=task.id, description=task.description, completed=task.completed)

@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, updated_task: TaskCreate):
    task_db = task_repo.get_by_id(task_id)
    if task_db is None:
        raise HTTPException(status_code=404, detail="Task not found")
        
    task = Task.Task(id=task_id, description=updated_task.description)
    task_repo.save(task)
    
    return TaskResponse(id=task.id, description=task.description, completed=task.completed)

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    deleted = task_repo.delete(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success"}
