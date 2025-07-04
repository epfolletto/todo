from fastapi import status

from todo.settings import settings


def test_login(client):
    response = client.post('/auth/login')

    assert response.status_code == status.HTTP_201_OK
    resp_json = response.json()['token']
    assert len(resp_json) == settings.EXPECTED_TOKEN_LENGTH
