from http.client import HTTPException, HTTPResponse

from celery.bin.result import result
from dns.e164 import query
from fastapi.openapi.models import Response
from sqlalchemy import select
from db.database import new_session
from db.transistotr_orm import TransistorOrm, TypeTransistorOrm, KorpusTransistorOrm
from schemas.transisnors import STransistorAdd, STypeTransistorAdd, SKorpusTransistorAdd


# Добавление транзистора
class TransistorRepository:
    @classmethod
    async def add_one(cls, data: STransistorAdd) -> int:
        async with new_session() as session:
            transistor_dict = data.model_dump()
            transistor = TransistorOrm(**transistor_dict)
            session.add(transistor)
            await session.flush()
            await session.commit()
            return transistor.id

# Редактирование транзистора
    @classmethod
    async def update_one(cls, data: STransistorAdd, id_tr):
        async with new_session() as session:
            try:
                query = select(TransistorOrm).where(TransistorOrm.id == id_tr)
                result = await session.execute(query)
                transistor_model = result.scalar_one()
                transistor_dict = data.model_dump()
                transistor = TransistorOrm(**transistor_dict)
                transistor_model.name = transistor.name
                transistor_model.markname = transistor.markname
                transistor_model.type_ = transistor.type_
                transistor_model.korpus = transistor.korpus
                transistor_model.descr = transistor.descr
                transistor_model.amount = transistor.amount
                transistor_model.path_file = transistor.path_file
                await session.flush()
                await session.commit()
                return transistor
            except Exception as err:
                return {'content': err, 'status_code': '404'}

# Получить транзистор по id
    @classmethod
    async def find_one(cls, id_tr: int) -> TransistorOrm:
        async with new_session() as session:
            try:
                query = select(TransistorOrm).where(TransistorOrm.id == id_tr)
                result = await session.execute(query)
                transistor_model = result.scalar_one()
                return transistor_model
            except Exception as err:
                return {'content': err, 'status_code': '404'}


#Список всех транзисторов
    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TransistorOrm)
            result = await session.execute(query)
            transistor_models = result.scalars().all()
            return transistor_models

# Добавление типа транзистора
    @classmethod
    async def add_type_one(cls, data: STypeTransistorAdd) -> int:
        async with new_session() as session:
            transistor_dict = data.model_dump()
            transistor = TypeTransistorOrm(**transistor_dict)
            session.add(transistor)
            await session.flush()
            await session.commit()
            return transistor.id

# Список всех типов
    @classmethod
    async def find_type_all(cls):
        async with new_session() as session:
            query = select(TypeTransistorOrm)
            result = await session.execute(query)
            type_models = result.scalars().all()
            return type_models


# Добавление корпуса транзистора
    @classmethod
    async def add_korpus_one(cls, data: SKorpusTransistorAdd) -> int:
        async with new_session() as session:
            transistor_dict = data.model_dump()
            transistor = KorpusTransistorOrm(**transistor_dict)
            session.add(transistor)
            await session.flush()
            await session.commit()
            return transistor.id

# Список всех корпусов
    @classmethod
    async def find_korpus_all(cls):
        async with new_session() as session:
            query = select(KorpusTransistorOrm)
            result = await session.execute(query)
            korpus_models = result.scalars().all()
            return korpus_models
