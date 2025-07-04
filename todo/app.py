from fastapi import FastAPI

from todo.routers import auth, todos

app = FastAPI(title='todo list')

app.include_router(todos.router)
app.include_router(auth.router)
