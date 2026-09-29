from typing import Optional
from pydantic import BaseModel, ConfigDict


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    model_config = ConfigDict(from_attributes=True)