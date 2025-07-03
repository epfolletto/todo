from fastapi import FastAPI

from todo.routers import todos

app = FastAPI(title='todo list')

app.include_router(todos.router)
