from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    password: Optional[str] = None
    status: int = 0


class STask(STaskAdd):
    id: int
