from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Health Check API
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Greeting API
@app.get("/greet")
def greet(name: str = "anonymous"):
    return {"message": f"Hello, {name}!"}

# TODO Create API
class TodoItem(BaseModel):
    title: str
    done: bool

class TodoResponse(TodoItem):
    id: int

todos = []

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoItem):
    new_todo = {"id": len(todos) + 1, **todo.model_dump()}
    todos.append(new_todo)
    return new_todo
