from fastapi import APIRouter, status

from todo.schemas import LoginSchemaOutput
from todo.security import generate_token

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post(
    '/login',
    response_model=LoginSchemaOutput,
    status_code=status.HTTP_200_OK
)
def login():
    token = generate_token()

    return {
        'token': token
    }
