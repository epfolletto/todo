import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from todo.app import app
from todo.database import get_session
from todo.models import table_registry
from todo.settings import settings


@pytest.fixture
def payload_create_todo():
    return {
        'title': 'test task',
        'description': 'this is a test task',
    }


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        # a linha abaixo troca para a session de testes
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(settings.DATABASE_URL_TEST)

    # Cria as tabelas no banco de teste
    table_registry.metadata.create_all(bind=engine)

    # Cria uma sessão SQLAlchemy
    TestingSessionLocal = sessionmaker(bind=engine)
    db: Session = TestingSessionLocal()

    yield db

    db.close()
    table_registry.metadata.drop_all(bind=engine)


@pytest.fixture
def token(client):
    response = client.post('/auth/login')
    return response.json()['token']
