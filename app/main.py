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

todos = {}  # {id: TodoItem}
next_id = 1

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoItem):
    global next_id
    todos[next_id] = {"id": next_id, **todo.model_dump()}
    result = todos[next_id]
    next_id += 1
    return result

# TODO 一覧表示 API
@app.get("/todos")
def get_todos():
    return list(todos.values())

# TODO 削除 API
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"message": "Deleted"}


