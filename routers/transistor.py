from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from reposytory.transistorrep import TransistorRepository
from schemas.transisnors import STransistorAdd, STypeTransistorAdd, SKorpusTransistorAdd

router = APIRouter(
    prefix="/transistor",
    tags=["Транзисторы"],
)

# Добавление транзистора в базу
@router.post("")
async def add_transistor(
    transistor: Annotated[STransistorAdd, Depends()]
):
    transistor_id = await TransistorRepository.add_one(transistor)
    return {"ok": True, "transistor_id": transistor_id,}

# Обновление транзистора
@router.put("/{id_tr}")
async def update_transistor(
    transistor: Annotated[STransistorAdd, Depends()],
    id_tr: int
):
    transistor_id = await TransistorRepository.update_one(transistor, id_tr)
    return {"ok": True, "transistor_id": transistor_id,"id": id_tr, }

# Получить транзистор по id
@router.get("/{id_tr}")
async def get_one(id_tr: int):
    transistor = await TransistorRepository.find_one(id_tr)
    return {'transistor': transistor}

# Получение списка транзисторов
@router.get("")
async def get_transistor():
    transistors = await TransistorRepository.find_all()
    return {'transistors': transistors}

# Добавление типа транзистора
@router.post("/type")
async def add_type_transistor(
    type_transistor: Annotated[STypeTransistorAdd, Depends()]
):
    transistor_id = await TransistorRepository.add_type_one(type_transistor)
    return {"ok": True, "task_id": transistor_id,}

# Получение списка типов
@router.get("/type")
async def get_type_transistor():
    type_transistors = await TransistorRepository.find_type_all()
    return {'type_': type_transistors}

# Добавление корпуса транзистора
@router.post("/korpus")
async def add_korpus_transistor(
    korpus_transistor: Annotated[SKorpusTransistorAdd, Depends()]
):
    transistor_id = await TransistorRepository.add_korpus_one(korpus_transistor)
    return {"ok": True, "korpus_id": transistor_id,}

# получение списка корпусов
@router.get("/korpus")
async def get_korpus_transistor():
    korpus_transistors = await TransistorRepository.find_korpus_all()
    return {'transistors': korpus_transistors}
