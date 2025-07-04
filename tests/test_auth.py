from fastapi import status


def test_login(client):
    response = client.post('/auth/login')

    EXPECTED_TOKEN_LENGTH = 9

    assert response.status_code == status.HTTP_200_OK
    resp_json = response.json()['token']
    assert len(resp_json) == EXPECTED_TOKEN_LENGTH
