import pytest
from pydantic import ValidationError

from todo.schemas import TodoSchemaInput


def test_input_data_iof_price_valid_data(payload_create_todo):
    data = TodoSchemaInput(**payload_create_todo)

    assert data.title == 'test task'
    assert data.description == 'this is a test task'


def test_fail_input_title_not_str(payload_create_todo):
    payload_create_todo['title'] = 1

    with pytest.raises(ValidationError):
        TodoSchemaInput(**payload_create_todo)


def test_fail_input_description_not_str(payload_create_todo):
    payload_create_todo['description'] = 1

    with pytest.raises(ValidationError):
        TodoSchemaInput(**payload_create_todo)
