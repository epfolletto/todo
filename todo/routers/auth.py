from fastapi import APIRouter

from todo.schemas import LoginSchemaOutput
from todo.secutiry import generate_token

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login', response_model=LoginSchemaOutput)
def login():
    token = generate_token()

    return {
        'token': token
    }
