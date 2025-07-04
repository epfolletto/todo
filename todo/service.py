from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from todo.models import Todo
from todo.schemas import TodoSchemaInput


def create_todo_service(todo: TodoSchemaInput, session: Session) -> Todo:
    todo_db = Todo(title=todo.title, description=todo.description)
    session.add(todo_db)
    session.commit()
    session.refresh(todo_db)
    return todo_db


def get_all_todos_service(session: Session) -> list[Todo]:
    return session.scalars(select(Todo)).all()


def get_todo_by_id_service(id: int, session: Session) -> Todo:
    todo = session.scalars(select(Todo).where(Todo.id == id)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


def update_todo_service(
    id: int,
    new_data: TodoSchemaInput,
    session: Session
) -> Todo:
    todo = get_todo_by_id_service(id, session)
    todo.title = new_data.title
    todo.description = new_data.description
    session.commit()
    session.refresh(todo)
    return todo


def delete_todo_service(id: int, session: Session) -> Todo:
    todo = get_todo_by_id_service(id, session)
    session.delete(todo)
    session.commit()
    return todo
