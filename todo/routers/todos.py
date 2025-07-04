from fastapi import APIRouter, Depends, status

from todo.database import get_session
from todo.schemas import (
    TodoSchemaGetAllOutput,
    TodoSchemaInput,
    TodoSchemaOutput,
)
from todo.security import validate_token
from todo.service import (
    create_todo_service,
    delete_todo_service,
    get_all_todos_service,
    get_todo_by_id_service,
    update_todo_service,
)

router = APIRouter(prefix='/todos', tags=['todos'])


@router.post(
    '/create',
    response_model=TodoSchemaOutput,
    status_code=status.HTTP_201_CREATED
)
def create_todo(
    todo: TodoSchemaInput,
    session=Depends(get_session),
    token=Depends(validate_token)
):
    todo_db = create_todo_service(todo, session)
    return {
        'msg': 'Task inserted with successfully!',
        'id': todo_db.id
    }


@router.get(
    '/all',
    response_model=list[TodoSchemaGetAllOutput],
    status_code=status.HTTP_200_OK
)
def all_todos(
    session=Depends(get_session),
    token=Depends(validate_token)
):
    todos = get_all_todos_service(session)

    return todos


@router.get(
    '/{id}',
    response_model=TodoSchemaGetAllOutput,
    status_code=status.HTTP_200_OK
)
def get_todo_by_id(
    id: int,
    session=Depends(get_session),
    token=Depends(validate_token)
):
    todo = get_todo_by_id_service(id, session)

    return todo


@router.put(
    '/{id}',
    response_model=TodoSchemaOutput,
    status_code=status.HTTP_200_OK
)
def put_todo(
    id: int,
    todo: TodoSchemaInput,
    session=Depends(get_session),
    token=Depends(validate_token)
):
    todo_updated = update_todo_service(id, todo, session)

    return {
        'msg': 'Task updated successfully',
        'id': todo_updated.id
    }


@router.delete(
    '/{id}',
    response_model=TodoSchemaOutput,
    status_code=status.HTTP_200_OK
)
def delete_todo(
    id: int,
    session=Depends(get_session),
    token=Depends(validate_token)
):
    todo_deleted = delete_todo_service(id, session)

    return {
        'msg': 'Task deleted successfully',
        'id': todo_deleted.id
    }
