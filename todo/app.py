from fastapi import FastAPI

from todo.routers import todos, auth

app = FastAPI(title='todo list')

app.include_router(todos.router)
app.include_router(auth.router)
