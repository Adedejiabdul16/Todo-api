from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db

app = FastAPI(title="Simple To-Do API")

app = FastAPI(title="Simple To-Do API")


@app.get("/")
def home():
    return {"message": "To-Do API is running. Go to /docs for Swagger UI."}


@app.post("/todos", response_model=schemas.TodoOut, status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    new_todo = models.Todo(title=todo.title, description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.get("/todos", response_model=List[schemas.TodoOut])
def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@app.get("/todos/{todo_id}", response_model=schemas.TodoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=schemas.TodoOut)
def update_todo(todo_id: int, data: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}