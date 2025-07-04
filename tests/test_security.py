import pytest
from fastapi import HTTPException
from todo.security import validate_token

import pytest

def test_validate_token_missing_header():
    with pytest.raises(HTTPException) as exc_info:
        validate_token(x_token=None)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Missing Authorization header"


def test_validate_token_missing_Bearer_term():
    with pytest.raises(HTTPException) as exc_info:
        validate_token(x_token='12345')

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid or missing Authorization header"


def test_validate_token_invalid_length():
    with pytest.raises(HTTPException) as exc_info:
        validate_token(x_token='Bearer 12345')

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token length"
