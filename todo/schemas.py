from datetime import datetime

from pydantic import BaseModel


class TodoSchemaInput(BaseModel):
    title: str
    description: str


class TodoSchemaOutput(BaseModel):
    msg: str
    id: int


class LoginSchemaOutput(BaseModel):
    token: int


class TodoSchemaGetAllOutput(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
