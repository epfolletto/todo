from todo.settings import settings

def test_login(client):
    response = client.post('/auth/login')

    assert response.status_code == 200
    resp_json = response.json()['token']
    assert len(resp_json) == settings.EXPECTED_TOKEN_LENGTH