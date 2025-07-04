# TODO

API para gerenciamento de atividades (todo list)

## Ferramentas e tecnologias
- [FastAPI](https://fastapi.tiangolo.com/) — Framework para criação de APIs web com suporte a operações assíncronas
- [Poetry](https://python-poetry.org/) — Gerenciador de dependências e ambiente virtual do projeto
- [Ruff](https://docs.astral.sh/ruff/) — Ferramenta de linting e formatação de código Python
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM utilizado para mapeamento objeto-relacional e consultas ao banco de dados
- [Taskipy](https://github.com/taskipy/taskipy) — Utilitário para criação e execução de tarefas via linha de comando


## Requisitos

- Python 3.12
- Poetry
- PostgreSQL


### Instalar dependências com Poetry

```bash
# Configurar o Poetry para usar Python 3.12
poetry env use 3.12

# Instalar dependências
poetry install --no-root
```

### Configurar variáveis de ambiente

Edite o nome do arquivo `.env.example` para `.env` e edite-o com as variáveis.

OBS:
- `DATABASE_URL` - Bancos de dados principal da aplicação
- `DATABASE_URL_TESTS` - Banco de dados de testes

### Aplicar as migrações
```bash
poetry run alembic upgrade head
```

### Rodar a aplicação
```bash
poetry run task run
```
A aplicação ficará disponível em: http://127.0.0.1:8000

- 📘 Documentação interativa (Swagger UI): http://127.0.0.1:8000/docs
- 📚 Documentação descritiva (ReDoc): http://127.0.0.1:8000/redoc


### Rodar testes
```bash
poetry run task test
```

### Rodar testes com relatório em html
```bash
poetry run task test_html
```

### Abrir relatório gerado em html
```bash
poetry run task open_html
```