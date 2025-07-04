import random
import time
from typing import Annotated

from fastapi import Header, HTTPException, status


def generate_token():
    number_1 = str(random.randint(1000, 9999))
    timestamp = str(time.time())

    token = number_1 + timestamp[:5]

    return token


def validate_token(x_token: Annotated[str, Header(...)]):
    if x_token is None:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization header"
        )

    if not x_token.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Authorization header",
        )

    token = x_token.removeprefix("Bearer ").strip()

    EXPECTED_TOKEN_LENGTH = 9
    if len(token) != EXPECTED_TOKEN_LENGTH:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token length",
        )

    return {'token': x_token}
