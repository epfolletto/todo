from fastapi import APIRouter

from todo.schemas import LoginSchemaOutput
from todo.security import generate_token
from fastapi import status

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
