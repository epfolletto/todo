import pytest


@pytest.fixture
def payload_create_todo():
    return {
        'title': 'test task',
        'description': 'this is a test task',
    }
