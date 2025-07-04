from fastapi import status


def get_bearer_token(token):
    return f'Bearer {token}'


def test_create_todo(client, token):
    bearer = get_bearer_token(token)
    response = client.post(
        '/todos/create',
        headers={'x-token': bearer},
        json={
            'title': 'Test todo',
            'description': 'Test todo description',
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == 1
    assert response.json()['msg'] == 'Task inserted with successfully!'


def test_list_todos(client, session, token, sample_todos):
    bearer = get_bearer_token(token)
    response = client.get('/todos/all',
        headers={'x-token': bearer},
    )

    assert response.status_code == status.HTTP_200_OK

    EXPECTED_LEN_TODOS = 2

    todos = response.json()
    assert len(todos) >= EXPECTED_LEN_TODOS
    titles = [t['title'] for t in todos]
    assert "Todo 1" in titles
    assert "Todo 2" in titles


def test_get_todo_by_id(client, session, token, sample_todos):
    bearer = get_bearer_token(token)
    response = client.get('/todos/1',
        headers={'x-token': bearer},
    )

    assert response.status_code == status.HTTP_200_OK

    todo = response.json()
    assert todo['title'] == "Todo 1"
    assert todo['description'] == "Description todo 1"


def test_get_todo_by_id_not_found(client, session, token, sample_todos):
    bearer = get_bearer_token(token)
    response = client.get('/todos/3',
        headers={'x-token': bearer},
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    todo = response.json()
    assert todo['detail'] == "Todo not found"


def test_update_todo_by_id(client, session, token, sample_todos):
    bearer = get_bearer_token(token)
    response = client.put('/todos/1',
        headers={'x-token': bearer},
        json={
            'title': 'Todo 1 updated',
            'description': 'Description todo 1 updated',
        },
    )

    assert response.status_code == status.HTTP_200_OK
    todo = response.json()
    assert todo['msg'] == "Task updated successfully"
    assert todo['id'] == todo['id']


def test_delete_todo(client, session, token, sample_todos):
    bearer = get_bearer_token(token)
    response = client.delete('/todos/2',
        headers={'x-token': bearer},
    )

    assert response.status_code == status.HTTP_200_OK
    todo = response.json()
    assert todo['msg'] == "Task deleted successfully"
    assert todo['id'] == todo['id']
