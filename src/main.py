from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

api = FastAPI()

class Todo(BaseModel):
    id: int
    name: str
    des: str
todos: List[Todo] = []

@api.get("/")
def read_root():
    return {"msg": "Welcome to Todo API"}

@api.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@api.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    for t in todos:
        if t.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    todos.append(todo)
    return todo

@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            deleted = todos.pop(i)
            return {"msg": f"Todo {deleted.id} deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
