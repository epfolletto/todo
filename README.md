# TODO

API para gerenciamento de atividades (todo list)

## Funcionamento da aplicação
A aplicação não possui um sistema de cadastro de usuários. A obtenção de um token é feita utilizando a rota `/auth/login` e então este token deve ser adicionado no header para as demais rotas, da seguinte forma:
- se for utilizada a documentação `/docs` para fazer requisições, basta adicionar "Bearer seu_token_aqui"
- se for utilizada uma ferramenta de envio de requisições, como o Postman, deve-se adicionar, nos headers:
    - **Key**: x-token
    - **Value**: Bearer seu_token_aqui

## Ferramentas e tecnologias
- [FastAPI](https://fastapi.tiangolo.com/) — Framework para criação de APIs web com suporte a operações assíncronas
- [Poetry](https://python-poetry.org/) — Gerenciador de dependências e ambiente virtual do projeto
- [Ruff](https://docs.astral.sh/ruff/) — Ferramenta de linting e formatação de código Python
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM utilizado para mapeamento objeto-relacional e consultas ao banco de dados
- [PostgreSQL](https://www.postgresql.org/) — Banco de dados
- [Taskipy](https://github.com/taskipy/taskipy) — Utilitário para criação e execução de tarefas via linha de comando


## Requisitos

- Python 3.12
- Poetry
- PostgreSQL


## Instalação

1. Clonar repositório

    ```bash
    git clone https://github.com/epfolletto/todo.git
    ```

2. Navegar até o diretório

    ```bash
    cd todo
    ```

3. Configurar o Poetry para usar Python 3.12

    ```bash
    poetry env use 3.12
    ```

4. Instalar dependências com Poetry

    ```bash
    poetry install --no-root
    ```


## Banco de dados
Você deve criar dois bancos de dados em PostgreSQL: um para a aplicação e outro para testes.


## Configurar variáveis de ambiente
Edite o nome do arquivo `.env.example` para `.env` e edite as seguintes variáveis `DATABASE_URL` e `DATABASE_URL_TEST`, onde:
- `user` - nome do usuário
- `password` - senha do usuário
- `database` - nome do banco de dados da aplicação
- `database_test` - nome do banco de dados de testes


## Aplicar as migrações
```bash
poetry run alembic upgrade head
```

## Rodar a aplicação
```bash
poetry run task run
```
A aplicação ficará disponível em: http://127.0.0.1:8000

- 📘 Documentação interativa (Swagger UI): http://127.0.0.1:8000/docs
- 📚 Documentação descritiva (ReDoc): http://127.0.0.1:8000/redoc



## Testes

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