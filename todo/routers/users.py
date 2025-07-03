from fastapi import APIRouter


router = APIRouter(prefix='/users', tags=['users'])


@router.get('/')
def hello_word():
    return 'ok'