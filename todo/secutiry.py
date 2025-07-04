from fastapi import HTTPException, Header, status
import random
from typing import Annotated
import time


def generate_token():
    number_1 = str(random.randint(0, 1000))
    timestamp = int(time.time())

    token = int(number_1 + str(timestamp))
    
    return token


def validate_token(x_token: Annotated[str, Header(...)]):
    if x_token is None:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if not x_token.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Authorization header",
        )

    token = x_token.removeprefix("Bearer ").strip()

    if len(token) != 13:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token length",
        )

    return {'token': x_token}
