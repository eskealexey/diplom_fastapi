from typing import Optional
from pydantic import BaseModel


class STransistorAdd(BaseModel):
    name: str
    markname: Optional[str] = None
    type_: Optional[int]
    korpus: Optional[int] = None
    descr: Optional[str] = None
    amount: Optional[int] = 0
    path_file: Optional[str] = None
    userid: Optional[int] = None


class STransistor(STransistorAdd):
    id: int


class STypeTransistorAdd(BaseModel):
    type_: str


class STypeTransistor(STypeTransistorAdd):
    type_: str