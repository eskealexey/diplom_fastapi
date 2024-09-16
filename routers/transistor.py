from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import session
from sqlalchemy.orm import Session

from typing_extensions import Annotated

from db.database import get_db
from db.transistotr_orm import TypeTransistorOrm
from reposytory.transistorrep import TransistorRepository
from schemas.transisnors import STransistorAdd, STypeTransistorAdd

router = APIRouter(
    prefix="/transistor",
    tags=["Транзисторы"],
)

@router.post("")
async def add_transistor(
    transistor: Annotated[STransistorAdd, Depends()]
):
    transistor_id = await TransistorRepository.add_one(transistor)
    return {"ok": True, "task_id": transistor_id,}


@router.get("")
async def get_transistor():
    transistors = await TransistorRepository.find_all()
    return {'transistors': transistors}


@router.post("/type")
async def add_type_transistor(
    type_transistor: Annotated[STypeTransistorAdd, Depends()]
):
    transistor_id = await TransistorRepository.add_type_one(type_transistor)
    return {"ok": True, "task_id": transistor_id,}



@router.get("/type")
async def get_type_transistor():
    type_transistors = await TransistorRepository.find_type_all()
    return {'transistors': type_transistors}
