from fastapi import FastAPI

from todo.routers import users

app = FastAPI(title='todo list')

app.include_router(users.router)
